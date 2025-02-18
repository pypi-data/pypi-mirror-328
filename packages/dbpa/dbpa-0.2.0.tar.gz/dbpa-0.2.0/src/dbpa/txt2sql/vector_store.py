"""Vector store for query examples and training data."""
from typing import Dict, List, Optional, Union, Any
from pydantic import BaseModel
import numpy as np
from pathlib import Path
import json
import faiss
import torch
from sentence_transformers import SentenceTransformer
import pandas as pd
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


class QueryExample(BaseModel):
    """Query example for training and reference."""
    natural_query: str
    sql_query: str
    language: str
    database_type: str
    schema_hash: str  # Hash of the schema when this example was created
    metadata: Dict[str, Any]
    embedding: Optional[List[float]] = None
    performance_metrics: Optional[Dict[str, float]] = None
    created_at: datetime = None
    last_used: datetime = None
    usage_count: int = 0
    success_rate: float = 1.0

    def __init__(self, **data):
        super().__init__(**data)
        if self.created_at is None:
            self.created_at = datetime.now()
        if self.last_used is None:
            self.last_used = self.created_at


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
        self.model = SentenceTransformer(model_name)
        self.dimension = dimension
        self.index = faiss.IndexFlatL2(dimension) if index_type == "L2" else faiss.IndexFlatIP(dimension)
        self.examples: Dict[int, QueryExample] = {}
        self.next_id = 0

    def add_example(self, example: QueryExample) -> int:
        """Add a query example to the store."""
        if example.embedding is None:
            example.embedding = self._compute_embedding(example.natural_query)
        
        example_id = self.next_id
        self.examples[example_id] = example
        self.index.add(np.array([example.embedding], dtype=np.float32))
        self.next_id += 1
        return example_id

    def search(
        self,
        query: str,
        k: int = 5,
        filters: Optional[Dict[str, Any]] = None
    ) -> List[QueryExample]:
        """Search for similar query examples."""
        query_embedding = self._compute_embedding(query)
        distances, indices = self.index.search(
            np.array([query_embedding], dtype=np.float32),
            k
        )
        
        results = []
        for idx in indices[0]:
            if idx != -1:  # Valid index
                example = self.examples[int(idx)]
                if self._matches_filters(example, filters):
                    example.last_used = datetime.now()
                    example.usage_count += 1
                    results.append(example)
        
        return results

    def _compute_embedding(self, text: str) -> List[float]:
        """Compute embedding for text."""
        with torch.no_grad():
            embedding = self.model.encode(text)
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

    def update_metrics(
        self,
        example_id: int,
        success: bool,
        execution_time: Optional[float] = None
    ) -> None:
        """Update example metrics after usage."""
        if example_id in self.examples:
            example = self.examples[example_id]
            
            # Update success rate
            total_uses = example.usage_count
            example.success_rate = (
                (example.success_rate * (total_uses - 1) + int(success)) / total_uses
            )
            
            # Update performance metrics
            if execution_time and example.performance_metrics:
                metrics = example.performance_metrics
                metrics["avg_execution_time"] = (
                    (metrics["avg_execution_time"] * (total_uses - 1) + execution_time)
                    / total_uses
                )
                metrics["min_execution_time"] = min(
                    metrics["min_execution_time"], execution_time
                )
                metrics["max_execution_time"] = max(
                    metrics["max_execution_time"], execution_time
                )

    def save(self, directory: Union[str, Path]) -> None:
        """Save vector store to directory."""
        directory = Path(directory)
        directory.mkdir(parents=True, exist_ok=True)
        
        # Save index
        faiss.write_index(self.index, str(directory / "index.faiss"))
        
        # Save examples
        examples_data = {
            str(idx): example.dict() for idx, example in self.examples.items()
        }
        with open(directory / "examples.json", "w") as f:
            json.dump(examples_data, f, indent=2, default=str)
        
        # Save metadata
        metadata = {
            "next_id": self.next_id,
            "dimension": self.dimension,
            "model_name": self.model.get_sentence_embedding_dimension()
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
        instance.index = faiss.read_index(str(directory / "index.faiss"))
        
        # Load examples
        with open(directory / "examples.json", "r") as f:
            examples_data = json.load(f)
            for idx_str, example_data in examples_data.items():
                idx = int(idx_str)
                instance.examples[idx] = QueryExample(**example_data)
                instance.next_id = max(instance.next_id, idx + 1)
        
        return instance

    def analyze_performance(self) -> pd.DataFrame:
        """Analyze performance of stored examples."""
        data = []
        for idx, example in self.examples.items():
            data.append({
                "id": idx,
                "language": example.language,
                "database_type": example.database_type,
                "usage_count": example.usage_count,
                "success_rate": example.success_rate,
                "avg_execution_time": example.performance_metrics.get("avg_execution_time") if example.performance_metrics else None,
                "last_used": example.last_used,
                "created_at": example.created_at
            })
        return pd.DataFrame(data)
