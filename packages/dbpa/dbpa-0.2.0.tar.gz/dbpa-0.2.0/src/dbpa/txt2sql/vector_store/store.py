"""Vector store implementation for semantic search of query examples."""
from typing import Dict, List, Optional, Union, Any
from pathlib import Path
import json
import faiss
import torch
import numpy as np
from numpy.typing import NDArray
from sentence_transformers import SentenceTransformer
import pandas as pd
import logging
from datetime import datetime

from dbpa.txt2sql.models.examples import QueryExample, PerformanceMetrics

logger = logging.getLogger(__name__)


class VectorStore:
    """Vector store for semantic search of query examples."""

    def __init__(
        self,
        model_name: str = "sentence-transformers/all-MiniLM-L6-v2",
        dimension: int = 384,
        index_type: str = "L2"
    ):
        """Initialize vector store.
        
        Args:
            model_name: Name of the sentence transformer model
            dimension: Embedding dimension
            index_type: FAISS index type (L2 or IP for inner product)
        """
        self._model = SentenceTransformer(model_name)
        self._dimension = dimension
        self._index = faiss.IndexFlatL2(dimension) if index_type == "L2" else faiss.IndexFlatIP(dimension)
        self._examples: Dict[int, QueryExample] = {}
        self._next_id = 0

    def add_example(self, example: QueryExample) -> int:
        """Add a query example to the store.
        
        Args:
            example: Query example to add
            
        Returns:
            ID of the added example
        """
        if example.embedding is None:
            example.embedding = self._compute_embedding(example.natural_query)
        
        example_id = self._next_id
        self._examples[example_id] = example
        self._index.add(self._to_numpy_array([example.embedding]))
        self._next_id += 1
        return example_id

    def search(
        self,
        query: str,
        k: int = 5,
        filters: Optional[Dict[str, Any]] = None
    ) -> List[QueryExample]:
        """Search for similar query examples.
        
        Args:
            query: Natural language query to search for
            k: Number of results to return
            filters: Optional filters to apply
            
        Returns:
            List of similar query examples
        """
        query_embedding = self._compute_embedding(query)
        distances, indices = self._index.search(
            self._to_numpy_array([query_embedding]),
            k
        )
        
        results = []
        for idx in indices[0]:
            if idx != -1:  # Valid index
                example = self._examples[int(idx)]
                if self._matches_filters(example, filters):
                    self._update_usage_stats(example)
                    results.append(example)
        
        return results

    def _compute_embedding(self, text: str) -> List[float]:
        """Compute embedding for text."""
        with torch.no_grad():
            embedding = self._model.encode(text)
            return embedding.tolist()

    def _matches_filters(
        self,
        example: QueryExample,
        filters: Optional[Dict[str, Any]]
    ) -> bool:
        """Check if example matches filters."""
        if not filters:
            return True
        
        for key, value in filters.items():
            if key == "language" and example.language != value:
                return False
            if key == "database_type" and example.database_type != value:
                return False
            if key == "schema_hash" and example.schema_hash != value:
                return False
            if key == "min_success_rate" and example.success_rate < value:
                return False
        return True

    def _update_usage_stats(self, example: QueryExample) -> None:
        """Update example usage statistics."""
        example.last_used = datetime.now()
        example.usage_count += 1

    def update_metrics(
        self,
        example_id: int,
        success: bool,
        execution_time: Optional[float] = None
    ) -> None:
        """Update example metrics after usage."""
        if example_id not in self._examples:
            return

        example = self._examples[example_id]
        total_uses = example.usage_count
        
        # Update success rate
        example.success_rate = (
            (example.success_rate * (total_uses - 1) + int(success)) / total_uses
        )
        
        # Update performance metrics
        if execution_time:
            if not example.performance_metrics:
                example.performance_metrics = PerformanceMetrics()
            
            metrics = example.performance_metrics
            metrics.avg_execution_time = (
                (metrics.avg_execution_time * (total_uses - 1) + execution_time)
                / total_uses
            )
            metrics.min_execution_time = min(metrics.min_execution_time, execution_time)
            metrics.max_execution_time = max(metrics.max_execution_time, execution_time)
            
            if success:
                metrics.success_count += 1
            else:
                metrics.error_count += 1

    @staticmethod
    def _to_numpy_array(embeddings: List[List[float]]) -> NDArray[np.float32]:
        """Convert embeddings to numpy array."""
        return np.array(embeddings, dtype=np.float32)

    def save(self, directory: Union[str, Path]) -> None:
        """Save vector store to directory."""
        directory = Path(directory)
        directory.mkdir(parents=True, exist_ok=True)
        
        # Save index
        faiss.write_index(self._index, str(directory / "index.faiss"))
        
        # Save examples
        examples_data = {
            str(idx): example.model_dump() for idx, example in self._examples.items()
        }
        with open(directory / "examples.json", "w") as f:
            json.dump(examples_data, f, indent=2, default=str)
        
        # Save metadata
        metadata = {
            "next_id": self._next_id,
            "dimension": self._dimension,
            "model_name": self._model.get_sentence_embedding_dimension()
        }
        with open(directory / "metadata.json", "w") as f:
            json.dump(metadata, f, indent=2)

    @classmethod
    def load(cls, directory: Union[str, Path]) -> "VectorStore":
        """Load vector store from directory."""
        directory = Path(directory)
        
        # Load metadata
        with open(directory / "metadata.json", "r") as f:
            metadata = json.load(f)
        
        # Create instance
        instance = cls(
            model_name=metadata["model_name"],
            dimension=metadata["dimension"]
        )
        
        # Load index
        instance._index = faiss.read_index(str(directory / "index.faiss"))
        
        # Load examples
        with open(directory / "examples.json", "r") as f:
            examples_data = json.load(f)
            for idx_str, example_data in examples_data.items():
                idx = int(idx_str)
                instance._examples[idx] = QueryExample.model_validate(example_data)
                instance._next_id = max(instance._next_id, idx + 1)
        
        return instance
