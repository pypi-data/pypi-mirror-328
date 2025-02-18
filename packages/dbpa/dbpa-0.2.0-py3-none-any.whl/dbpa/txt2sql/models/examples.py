"""Models for query examples and training data."""
from typing import Dict, List, Optional, Any
from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime


class PerformanceMetrics(BaseModel):
    """Performance metrics for query execution."""
    avg_execution_time: float = Field(0.0, description="Average execution time in seconds")
    min_execution_time: float = Field(float("inf"), description="Minimum execution time in seconds")
    max_execution_time: float = Field(0.0, description="Maximum execution time in seconds")
    error_count: int = Field(0, description="Number of execution errors")
    success_count: int = Field(0, description="Number of successful executions")

    model_config = ConfigDict(frozen=True)


class QueryExample(BaseModel):
    """Query example for training and reference."""
    natural_query: str = Field(..., description="Natural language query")
    sql_query: str = Field(..., description="Generated SQL query")
    language: str = Field(..., description="Language code (e.g., 'en', 'de')")
    database_type: str = Field(..., description="Database type (e.g., 'postgresql')")
    schema_hash: str = Field(..., description="Hash of the schema when example was created")
    metadata: Dict[str, Any] = Field(
        default_factory=dict,
        description="Additional metadata about the example"
    )
    embedding: Optional[List[float]] = Field(
        None,
        description="Vector embedding of the natural query"
    )
    performance_metrics: Optional[PerformanceMetrics] = Field(
        None,
        description="Query performance metrics"
    )
    created_at: datetime = Field(
        default_factory=datetime.now,
        description="Creation timestamp"
    )
    last_used: datetime = Field(
        default_factory=datetime.now,
        description="Last usage timestamp"
    )
    usage_count: int = Field(0, description="Number of times this example was used")
    success_rate: float = Field(1.0, description="Success rate of query execution")

    model_config = ConfigDict(
        validate_assignment=True,
        json_encoders={
            datetime: lambda v: v.isoformat()
        }
    )
