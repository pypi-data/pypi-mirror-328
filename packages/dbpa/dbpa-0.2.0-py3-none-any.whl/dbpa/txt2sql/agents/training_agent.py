"""Training agent for managing query examples and vector store."""
from typing import Dict, List, Optional, Any
import logging
from datetime import datetime

from dbpa.txt2sql.models.examples import QueryExample
from dbpa.txt2sql.vector_store.store import VectorStore

logger = logging.getLogger(__name__)


class TrainingAgent:
    """Agent for managing query examples and training data."""

    def __init__(
        self,
        vector_store: VectorStore,
        min_success_rate: float = 0.8,
        max_examples_per_schema: int = 1000
    ):
        """Initialize training agent.
        
        Args:
            vector_store: Vector store instance
            min_success_rate: Minimum success rate for examples
            max_examples_per_schema: Maximum examples per schema
        """
        self._store = vector_store
        self._min_success_rate = min_success_rate
        self._max_examples_per_schema = max_examples_per_schema
        self._schema_counts: Dict[str, int] = {}

    def add_example(
        self,
        natural_query: str,
        sql_query: str,
        language: str,
        database_type: str,
        schema_hash: str,
        metadata: Optional[Dict[str, Any]] = None
    ) -> Optional[int]:
        """Add a new query example.
        
        Args:
            natural_query: Natural language query
            sql_query: Generated SQL query
            language: Language code
            database_type: Database type
            schema_hash: Schema hash
            metadata: Optional metadata
            
        Returns:
            Example ID if added, None if rejected
        """
        # Check schema count limit
        if schema_hash in self._schema_counts:
            if self._schema_counts[schema_hash] >= self._max_examples_per_schema:
                logger.warning(
                    f"Schema {schema_hash} has reached maximum examples "
                    f"({self._max_examples_per_schema})"
                )
                return None
            self._schema_counts[schema_hash] += 1
        else:
            self._schema_counts[schema_hash] = 1

        # Create and add example
        example = QueryExample(
            natural_query=natural_query,
            sql_query=sql_query,
            language=language,
            database_type=database_type,
            schema_hash=schema_hash,
            metadata=metadata or {}
        )
        return self._store.add_example(example)

    def find_similar_examples(
        self,
        query: str,
        k: int = 5,
        language: Optional[str] = None,
        database_type: Optional[str] = None,
        schema_hash: Optional[str] = None,
        min_success_rate: Optional[float] = None
    ) -> List[QueryExample]:
        """Find similar query examples.
        
        Args:
            query: Natural language query
            k: Number of results
            language: Optional language filter
            database_type: Optional database type filter
            schema_hash: Optional schema hash filter
            min_success_rate: Optional minimum success rate
            
        Returns:
            List of similar examples
        """
        filters = {}
        if language:
            filters["language"] = language
        if database_type:
            filters["database_type"] = database_type
        if schema_hash:
            filters["schema_hash"] = schema_hash
        if min_success_rate is not None:
            filters["min_success_rate"] = min_success_rate
        
        return self._store.search(query, k=k, filters=filters)

    def update_example_metrics(
        self,
        example_id: int,
        success: bool,
        execution_time: Optional[float] = None
    ) -> None:
        """Update example metrics after usage.
        
        Args:
            example_id: Example ID
            success: Whether execution was successful
            execution_time: Optional execution time in seconds
        """
        self._store.update_metrics(
            example_id=example_id,
            success=success,
            execution_time=execution_time
        )

    def get_schema_stats(self, schema_hash: str) -> Dict[str, Any]:
        """Get statistics for a schema.
        
        Args:
            schema_hash: Schema hash
            
        Returns:
            Dictionary with schema statistics
        """
        examples = self._store.search(
            "",
            k=self._max_examples_per_schema,
            filters={"schema_hash": schema_hash}
        )
        
        total_examples = len(examples)
        if total_examples == 0:
            return {
                "total_examples": 0,
                "avg_success_rate": 0.0,
                "total_usage": 0
            }
        
        total_success_rate = sum(ex.success_rate for ex in examples)
        total_usage = sum(ex.usage_count for ex in examples)
        
        return {
            "total_examples": total_examples,
            "avg_success_rate": total_success_rate / total_examples,
            "total_usage": total_usage
        }

    def cleanup_examples(
        self,
        min_success_rate: Optional[float] = None,
        min_usage_count: Optional[int] = None
    ) -> int:
        """Remove low-quality examples.
        
        Args:
            min_success_rate: Minimum success rate to keep
            min_usage_count: Minimum usage count to keep
            
        Returns:
            Number of examples removed
        """
        min_success_rate = min_success_rate or self._min_success_rate
        removed = 0
        
        for example_id, example in list(self._store._examples.items()):
            if example.success_rate < min_success_rate:
                if min_usage_count is None or example.usage_count >= min_usage_count:
                    del self._store._examples[example_id]
                    removed += 1
                    
                    # Update schema count
                    self._schema_counts[example.schema_hash] -= 1
                    if self._schema_counts[example.schema_hash] == 0:
                        del self._schema_counts[example.schema_hash]
        
        return removed
