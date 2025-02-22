"""Deeplake vector store."""

from __future__ import annotations

import asyncio
from functools import partial
from typing import Any, Callable, Iterable, List, Optional, Tuple, Type, TypeVar
from uuid import uuid4

import deeplake
import numpy as np
from langchain_core.documents import Document
from langchain_core.embeddings import Embeddings
from langchain_core.vectorstores import VectorStore
from langchain_deeplake.filtering_util import attribute_based_filtering_tql
from langchain_deeplake.query import search
from langchain_deeplake.exceptions import (
    MissingQueryOrTQLError,
    InvalidQuerySpecificationError,
)

VST = TypeVar("VST", bound="DeeplakeVectorStore")


class DeeplakeVectorStore(VectorStore):
    """Deeplake vector store integration.

    Setup:
        Install ``langchain-deeplake`` package:

        .. code-block:: bash

            pip install -U langchain-deeplake

    Args:
        dataset_path: Path/URL to store the dataset
        embedding_function: Embedding model to use
        token: Optional Activeloop token
        read_only: Whether to open dataset in read-only mode
        creds: Optional cloud credentials for dataset access
        overwrite: Whether to overwrite existing dataset
    """

    def __init__(
        self,
        dataset_path: str,
        embedding_function: Optional[Embeddings] = None,
        token: Optional[str] = None,
        read_only: bool = False,
        creds: Optional[dict] = None,
        overwrite: bool = False,
    ) -> None:
        """Initialize Deeplake vector store."""
        self.embedding_function = embedding_function
        self.dataset_path = dataset_path
        self.token = token
        self.creds = creds

        try:
            exists = deeplake.exists(dataset_path, token=token, creds=creds)
        except Exception as e:
            exists = False

        if overwrite and exists:
            deeplake.delete(dataset_path, token=token, creds=creds)

        if exists and not overwrite:
            self.dataset = (
                deeplake.open(dataset_path, token=token, creds=creds)
                if not read_only
                else deeplake.open_read_only(dataset_path, token=token, creds=creds)
            )
        else:
            self.dataset = deeplake.create(
                dataset_path,
                token=token,
                creds=creds,
                schema={
                    "ids": deeplake.types.Text(),
                    "embeddings": deeplake.types.Embedding(),
                    "metadata": deeplake.types.Dict(),
                    "documents": deeplake.types.Text(),
                },
            )
            self.dataset.indexing_mode = deeplake.IndexingMode.Always

    def __len__(self) -> int:
        """Return the number of documents in the vector store."""
        return len(self.dataset)

    def add_texts(
        self,
        texts: Iterable[str],
        metadatas: Optional[List[dict]] = None,
        *,
        ids: Optional[List[str]] = None,
        **kwargs: Any,
    ) -> List[str]:
        """Add texts to the vector store."""
        # Convert iterator to list
        texts = list(texts)

        # Generate embeddings
        embeddings = self.embedding_function.embed_documents(texts)

        # Generate IDs if not provided
        if ids is None:
            ids = [str(uuid4()) for _ in texts]

        # Handle metadata
        if metadatas is None:
            metadatas = [{} for _ in texts]

        # Add to dataset
        self.dataset.append(
            {
                "ids": ids,
                "embeddings": embeddings,
                "metadata": metadatas,
                "documents": texts,
            }
        )
        self.dataset.commit()

        return ids

    @property
    def embeddings(self) -> Optional[Embeddings]:
        """Access the query embedding object if available."""
        return self.embedding_function

    def delete(self, ids: Optional[List[str]] = None, **kwargs: Any) -> Optional[bool]:
        """Delete documents by ID from the vector store."""
        if not ids:
            return False

        ids_str = ", ".join([f"'{i}'" for i in ids])
        # Query to find indices to delete
        query = (
            f"SELECT * FROM (SELECT *, ROW_NUMBER() as row_id) WHERE ids IN ({ids_str})"
        )
        results = self.dataset.query(query)

        if len(results) == 0:
            return False

        # Delete found documents
        for idx in sorted(results["row_id"][:], reverse=True):
            self.dataset.delete(idx)

        self.dataset.commit()
        return True

    def get_by_ids(self, ids: List[str], **kwargs: Any) -> List[Document]:
        """Return documents by ID."""
        ids_str = ", ".join([f"'{i}'" for i in ids])
        results = self.dataset.query(f"SELECT * WHERE ids IN ({ids_str})")
        docs = results["documents"][:]
        metadatas = results["metadata"][:]
        return [
            Document(page_content=docs[i], metadata=metadatas[i].to_dict(convert_numpy_to_list=True))
            for i in range(len(results))
        ]

    async def aget_by_ids(self, ids: List[str], **kwargs: Any) -> List[Document]:
        """Asynchronously return documents by ID."""
        return await asyncio.get_running_loop().run_in_executor(
            None, partial(self.get_by_ids, **kwargs), ids
        )

    async def adelete(
        self, ids: Optional[List[str]] = None, **kwargs: Any
    ) -> Optional[bool]:
        """Asynchronously delete documents by ID."""
        return await asyncio.get_running_loop().run_in_executor(
            None, partial(self.delete, **kwargs), ids
        )

    async def aadd_texts(
        self,
        texts: Iterable[str],
        metadatas: Optional[List[dict]] = None,
        *,
        ids: Optional[List[str]] = None,
        **kwargs: Any,
    ) -> List[str]:
        """Asynchronously add texts to the vector store."""
        return await asyncio.get_running_loop().run_in_executor(
            None, partial(self.add_texts, **kwargs), texts, metadatas, ids
        )

    def similarity_search(
        self, query: str, k: int = 4, filter: Optional[dict] = None, **kwargs: Any
    ) -> List[Document]:
        """Return documents most similar to query."""
        docs_with_scores = self.similarity_search_with_score(query, k, filter, **kwargs)
        return [doc for doc, _ in docs_with_scores]

    async def asimilarity_search(
        self, query: str, k: int = 4, filter: Optional[dict] = None, **kwargs: Any
    ) -> List[Document]:
        """Asynchronously return documents most similar to query."""
        func = partial(self.similarity_search, query, k=k, filter=filter, **kwargs)
        return await asyncio.get_running_loop().run_in_executor(None, func)

    def similarity_search_with_score(
        self,
        query: str,
        k: int = 4,
        filter: Optional[dict] = None,
        tql: Optional[str] = None,
        distance_metric: str = "cos",
        **kwargs: Any,
    ) -> List[Tuple[Document, Optional[float]]]:
        """Return documents most similar to query with scores."""
        if query is None and tql is None:
            raise MissingQueryOrTQLError()

        # if (query is None) == (tql is None):
        #     raise InvalidQuerySpecificationError()

        if query is None:
            query_embedding = None
        else:
            query_embedding = self.embedding_function.embed_query(query)

        tql = search(
            dataset=self.dataset,
            query_embedding=query_embedding,
            distance_metric=distance_metric,
            k=k,
            tql_string=tql,
            tql_filter=filter,
            embedding_tensor="embeddings",
            return_tensors=["documents", "metadata"],
        )

        results = self.dataset.query(tql)

        docs_with_scores_columnar = {
            "documents": results["documents"][:],
            "metadata": results["metadata"][:],
        }

        has_score = "score" in [col.name for col in results.schema.columns]
        if has_score:
            docs_with_scores_columnar["score"] = results["score"][:]

        docs_with_scores = []
        for i in range(len(results)):
            doc = Document(
                page_content=docs_with_scores_columnar["documents"][i],
                metadata=docs_with_scores_columnar["metadata"][i].to_dict(convert_numpy_to_list=True),
            )
            score = docs_with_scores_columnar["score"][i] if has_score else None
            docs_with_scores.append((doc, score))

        return docs_with_scores

    async def asimilarity_search_with_score(
        self, query: str, k: int = 4, filter: Optional[dict] = None, **kwargs: Any
    ) -> List[Tuple[Document, float]]:
        """Asynchronously return documents most similar to query with scores."""
        func = partial(
            self.similarity_search_with_score, query, k=k, filter=filter, **kwargs
        )
        return await asyncio.get_running_loop().run_in_executor(None, func)

    def max_marginal_relevance_search(
        self,
        query: str,
        k: int = 4,
        fetch_k: int = 20,
        lambda_mult: float = 0.5,
        **kwargs: Any,
    ) -> List[Document]:
        """Return documents selected using maximal marginal relevance."""
        query_embedding = self.embedding_function.embed_query(query)
        return self.max_marginal_relevance_search_by_vector(
            query_embedding, k=k, fetch_k=fetch_k, lambda_mult=lambda_mult, **kwargs
        )

    async def amax_marginal_relevance_search(
        self,
        query: str,
        k: int = 4,
        fetch_k: int = 20,
        lambda_mult: float = 0.5,
        **kwargs: Any,
    ) -> list[Document]:
        """Asynchronously return documents selected using maximal marginal relevance."""
        return await asyncio.get_running_loop().run_in_executor(
            None, partial(self.max_marginal_relevance_search, **kwargs)
        )

    def max_marginal_relevance_search_by_vector(
        self,
        embedding: List[float],
        k: int = 4,
        fetch_k: int = 20,
        lambda_mult: float = 0.5,
        **kwargs: Any,
    ) -> List[Document]:
        """Return docs selected using maximal marginal relevance by embedding."""
        emb_str = ", ".join([str(e) for e in embedding])
        # Get initial results
        results = self.dataset.query(
            f"""
            SELECT * FROM (SELECT documents, metadata, embeddings,
            COSINE_SIMILARITY(embeddings, ARRAY[{emb_str}]) as score)
            ORDER BY score DESC LIMIT {fetch_k}
        """
        )

        if len(results) == 0:
            return []

        # Extract embeddings and convert to numpy
        embeddings = results["embeddings"][:]

        # Calculate MMR
        selected_indices = []
        remaining_indices = list(range(len(embeddings)))

        for _ in range(min(k, len(embeddings))):
            if not remaining_indices:
                break

            # Calculate MMR scores
            if not selected_indices:
                similarities = results["score"][:]
                mmr_scores = similarities
            else:
                similarities = np.array(
                    [results[i]["score"] for i in remaining_indices]
                )
                selected_embeddings = embeddings[selected_indices]
                remaining_embeddings = embeddings[remaining_indices]

                # Calculate diversity penalty
                diversity_scores = np.max(
                    np.dot(remaining_embeddings, selected_embeddings.T), axis=1
                )
                mmr_scores = (
                    lambda_mult * similarities - (1 - lambda_mult) * diversity_scores
                )

            # Select next document
            next_idx = remaining_indices[np.argmax(mmr_scores)]
            selected_indices.append(next_idx)
            remaining_indices.remove(next_idx)

        # Return selected documents
        return [
            Document(
                page_content=results[i]["documents"], metadata=results[i]["metadata"]
            )
            for i in selected_indices
        ]

    def similarity_search_by_vector(
        self,
        embedding: Union[List[float], np.ndarray],
        k: int = 4,
        **kwargs: Any,
    ) -> List[Document]:
        """
        Return docs most similar to embedding vector.

        Examples:
            >>> # Search using an embedding
            >>> data = vector_store.similarity_search_by_vector(
            ...    embedding=<your_embedding>,
            ...    k=<num_items_to_return>,
            ... )

        Args:
            embedding (Union[List[float], np.ndarray]):
                Embedding to find similar docs.
            k (int): Number of Documents to return. Defaults to 4.
            kwargs: Additional keyword arguments including:
                filter (Union[Dict, Callable], optional):
                    Additional filter before embedding search.
                    - ``Dict`` - Key-value search on tensors of htype json. True
                        if all key-value filters are satisfied.
                        Dict = {"tensor_name_1": {"key": value},
                                "tensor_name_2": {"key": value}}
                    - ``Function`` - Any function compatible with
                        `deeplake.filter`.
                    Defaults to None.
                distance_metric (str): `L2` for Euclidean, `cos` for cosine similarity, Defaults to `cos`.

        Returns:
            List[Document]: List of Documents most similar to the query vector.
        """

        tql = search(
            dataset=self.dataset,
            query_embedding=embedding,
            distance_metric=(
                "cos"
                if "distance_metric" not in kwargs
                else kwargs["distance_metric"].lower()
            ),
            k=k,
            tql_string=kwargs.get("tql", None),
            tql_filter=kwargs.get("filter", None),
            embedding_tensor="embeddings",
            return_tensors=["embeddings", "metadata", "documents", "ids"],
        )

        results = self.dataset.query(tql)

        scores = results["score"][:]
        embeddings = results["embeddings"][:]
        metadatas = results["metadata"][:]
        texts = results["documents"][:]

        docs = [
            Document(
                page_content=text,
                metadata=metadata,
            )
            for text, metadata in zip(texts, metadatas)
        ]

        if "return_score" in kwargs and kwargs["return_score"]:
            if not isinstance(scores, list):
                scores = [scores]

            return [(doc, score) for doc, score in zip(docs, scores)]

        return docs

    def delete_dataset(self) -> None:
        deeplake.delete(self.dataset_path)

    @classmethod
    def from_texts(
        cls: Type[VST],
        texts: List[str],
        embedding: Embeddings,
        metadatas: Optional[List[dict]] = None,
        dataset_path: str = "mem://langchain",
        **kwargs: Any,
    ) -> VST:
        """Create DeeplakeVectorStore from raw texts."""
        store = cls(dataset_path=dataset_path, embedding_function=embedding, **kwargs)
        store.add_texts(texts=texts, metadatas=metadatas)
        return store

    @classmethod
    async def afrom_texts(
        cls: Type[VST],
        texts: List[str],
        embedding: Embeddings,
        metadatas: Optional[List[dict]] = None,
        dataset_path: str = "mem://langchain",
        **kwargs: Any,
    ) -> VST:
        """Asynchronously create DeeplakeVectorStore from raw texts."""
        store = cls(dataset_path=dataset_path, embedding_function=embedding, **kwargs)
        return await store.aadd_texts(texts=texts, metadatas=metadatas)

    def _select_relevance_score_fn(self) -> Callable[[float], float]:
        """Return relevance score function."""
        return lambda x: x  # Identity function since scores are already normalized

from langchain.retrievers.self_query.base import _get_builtin_translator
_original_get_builtin_translator = _get_builtin_translator

def _patched_get_builtin_translator(vectorstore):
    """Patched version of _get_builtin_translator to handle DeeplakeVectorStore type."""
    if isinstance(vectorstore, DeeplakeVectorStore):
        from langchain_community.query_constructors.deeplake import DeepLakeTranslator
        return DeepLakeTranslator()
    return _original_get_builtin_translator(vectorstore)

import langchain.retrievers.self_query.base
langchain.retrievers.self_query.base._get_builtin_translator = _patched_get_builtin_translator