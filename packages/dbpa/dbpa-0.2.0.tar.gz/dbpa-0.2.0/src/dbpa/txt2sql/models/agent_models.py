"""Models for agent-based text-to-SQL system."""
from typing import Dict, List, Optional, Any, Union
from enum import Enum
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict


class Risk(BaseModel):
    """Security risk model."""
    severity: str = Field(..., description="Risk severity level")
    description: str = Field(..., description="Risk description")
    location: str = Field(..., description="Location in query")
    suggestion: str = Field(..., description="Suggestion to fix")

    model_config = ConfigDict(frozen=True)


class Change(BaseModel):
    """Schema change model."""
    type: str = Field(..., description="Type of change")
    object: str = Field(..., description="Object that changed")
    details: str = Field(..., description="Change details")
    impact: List[str] = Field(default_factory=list, description="Impact on queries")

    model_config = ConfigDict(frozen=True)


class Suggestion(BaseModel):
    """Improvement suggestion model."""
    category: str = Field(..., description="Suggestion category")
    description: str = Field(..., description="Suggestion description")
    current: str = Field(..., description="Current state")
    proposed: str = Field(..., description="Proposed change")
    benefit: str = Field(..., description="Expected benefit")

    model_config = ConfigDict(frozen=True)


class ValidationResult(BaseModel):
    """Query validation result."""
    is_valid: bool = Field(..., description="Whether query is valid")
    errors: List[str] = Field(default_factory=list, description="Validation errors")
    warnings: List[str] = Field(default_factory=list, description="Validation warnings")
    suggestions: List[Suggestion] = Field(
        default_factory=list,
        description="Improvement suggestions"
    )

    model_config = ConfigDict(frozen=True)


class StyleIssue(BaseModel):
    """SQL style issue."""
    type: str = Field(..., description="Issue type")
    description: str = Field(..., description="Issue description")
    location: str = Field(..., description="Location in query")
    fix: str = Field(..., description="Suggested fix")

    model_config = ConfigDict(frozen=True)


class Template(BaseModel):
    """Query template."""
    name: str = Field(..., description="Template name")
    description: str = Field(..., description="Template description")
    natural_template: str = Field(..., description="Natural language template")
    sql_template: str = Field(..., description="SQL template")
    parameters: Dict[str, str] = Field(
        default_factory=dict,
        description="Template parameters"
    )
    metadata: Dict[str, Any] = Field(
        default_factory=dict,
        description="Additional metadata"
    )

    model_config = ConfigDict(frozen=True)


class Pattern(BaseModel):
    """Usage pattern."""
    pattern_type: str = Field(..., description="Pattern type")
    frequency: int = Field(..., description="Occurrence frequency")
    examples: List[int] = Field(..., description="Example IDs showing pattern")
    description: str = Field(..., description="Pattern description")
    confidence: float = Field(..., description="Pattern confidence score")

    model_config = ConfigDict(frozen=True)


class Metric(BaseModel):
    """Performance metric."""
    name: str = Field(..., description="Metric name")
    value: float = Field(..., description="Metric value")
    timestamp: datetime = Field(
        default_factory=datetime.now,
        description="Measurement timestamp"
    )
    metadata: Dict[str, Any] = Field(
        default_factory=dict,
        description="Additional metadata"
    )

    model_config = ConfigDict(frozen=True)


class Anomaly(BaseModel):
    """Performance anomaly."""
    metric: str = Field(..., description="Affected metric")
    value: float = Field(..., description="Anomalous value")
    expected_range: tuple[float, float] = Field(
        ...,
        description="Expected value range"
    )
    timestamp: datetime = Field(
        default_factory=datetime.now,
        description="Detection timestamp"
    )
    severity: str = Field(..., description="Anomaly severity")

    model_config = ConfigDict(frozen=True)


class Alert(BaseModel):
    """System alert."""
    level: str = Field(..., description="Alert level")
    message: str = Field(..., description="Alert message")
    timestamp: datetime = Field(
        default_factory=datetime.now,
        description="Alert timestamp"
    )
    source: str = Field(..., description="Alert source")
    metadata: Dict[str, Any] = Field(
        default_factory=dict,
        description="Additional metadata"
    )

    model_config = ConfigDict(frozen=True)


class Report(BaseModel):
    """Performance report."""
    period: str = Field(..., description="Report period")
    metrics: List[Metric] = Field(..., description="Performance metrics")
    anomalies: List[Anomaly] = Field(
        default_factory=list,
        description="Detected anomalies"
    )
    recommendations: List[Suggestion] = Field(
        default_factory=list,
        description="Improvement recommendations"
    )
    metadata: Dict[str, Any] = Field(
        default_factory=dict,
        description="Additional metadata"
    )

    model_config = ConfigDict(frozen=True)


class Plan(BaseModel):
    """Query execution plan."""
    steps: List[Dict[str, Any]] = Field(..., description="Plan steps")
    cost: float = Field(..., description="Estimated cost")
    timing: Dict[str, float] = Field(
        default_factory=dict,
        description="Step timing estimates"
    )
    recommendations: List[Suggestion] = Field(
        default_factory=list,
        description="Optimization recommendations"
    )

    model_config = ConfigDict(frozen=True)


class Documentation(BaseModel):
    """Query documentation."""
    description: str = Field(..., description="Query description")
    purpose: str = Field(..., description="Query purpose")
    parameters: Dict[str, str] = Field(
        default_factory=dict,
        description="Parameter descriptions"
    )
    examples: List[Dict[str, str]] = Field(
        default_factory=list,
        description="Usage examples"
    )
    notes: List[str] = Field(default_factory=list, description="Additional notes")

    model_config = ConfigDict(frozen=True)


class TestCase(BaseModel):
    """Query test case."""
    name: str = Field(..., description="Test case name")
    input_data: Dict[str, Any] = Field(..., description="Test input data")
    expected_output: Any = Field(..., description="Expected output")
    setup: Optional[str] = Field(None, description="Setup SQL")
    cleanup: Optional[str] = Field(None, description="Cleanup SQL")
    metadata: Dict[str, Any] = Field(
        default_factory=dict,
        description="Additional metadata"
    )

    model_config = ConfigDict(frozen=True)


class Coverage(BaseModel):
    """Test coverage information."""
    total_queries: int = Field(..., description="Total number of queries")
    tested_queries: int = Field(..., description="Number of tested queries")
    coverage_percent: float = Field(..., description="Coverage percentage")
    untested_scenarios: List[str] = Field(
        default_factory=list,
        description="Untested scenarios"
    )
    critical_paths: Dict[str, bool] = Field(
        default_factory=dict,
        description="Critical path coverage"
    )

    model_config = ConfigDict(frozen=True)


class AuditResult(BaseModel):
    """Query audit result."""
    timestamp: datetime = Field(
        default_factory=datetime.now,
        description="Audit timestamp"
    )
    query_hash: str = Field(..., description="Query hash")
    accessed_tables: List[str] = Field(..., description="Accessed tables")
    accessed_columns: Dict[str, List[str]] = Field(
        ...,
        description="Accessed columns by table"
    )
    sensitive_data: List[str] = Field(
        default_factory=list,
        description="Accessed sensitive data"
    )
    permissions_required: List[str] = Field(
        ...,
        description="Required permissions"
    )

    model_config = ConfigDict(frozen=True)


class ProcessedQuery(BaseModel):
    """Fully processed query with all agent results."""
    natural_query: str = Field(..., description="Original natural query")
    sql_query: str = Field(..., description="Generated SQL query")
    validation: ValidationResult = Field(..., description="Validation results")
    security: List[Risk] = Field(
        default_factory=list,
        description="Security checks"
    )
    performance: Plan = Field(..., description="Execution plan")
    documentation: Documentation = Field(..., description="Query documentation")
    tests: List[TestCase] = Field(
        default_factory=list,
        description="Generated tests"
    )
    audit: AuditResult = Field(..., description="Audit results")
    metadata: Dict[str, Any] = Field(
        default_factory=dict,
        description="Additional metadata"
    )

    model_config = ConfigDict(frozen=True)
