"""Base classes for text-to-SQL agents."""
from typing import Dict, List, Optional, Any, Protocol, runtime_checkable
from abc import ABC, abstractmethod
import logging
from datetime import datetime

from dbpa.txt2sql.models.agent_models import (
    ValidationResult, Risk, Change, Suggestion, StyleIssue,
    Template, Pattern, Metric, Anomaly, Alert, Report,
    Plan, Documentation, TestCase, Coverage, AuditResult
)

logger = logging.getLogger(__name__)


@runtime_checkable
class Agent(Protocol):
    """Base protocol for all agents."""
    
    def initialize(self) -> None:
        """Initialize agent resources."""
        ...

    def cleanup(self) -> None:
        """Cleanup agent resources."""
        ...

    def get_status(self) -> Dict[str, Any]:
        """Get agent status information."""
        ...


class BaseAgent(ABC):
    """Base implementation for agents."""

    def __init__(self, name: str):
        """Initialize base agent.
        
        Args:
            name: Agent name
        """
        self.name = name
        self._initialized = False
        self._start_time = None
        self._metrics: List[Metric] = []

    def initialize(self) -> None:
        """Initialize agent resources."""
        if self._initialized:
            return
        
        try:
            self._start_time = datetime.now()
            self._do_initialize()
            self._initialized = True
            logger.info(f"Agent {self.name} initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize agent {self.name}: {str(e)}")
            raise

    def cleanup(self) -> None:
        """Cleanup agent resources."""
        if not self._initialized:
            return
            
        try:
            self._do_cleanup()
            self._initialized = False
            logger.info(f"Agent {self.name} cleaned up successfully")
        except Exception as e:
            logger.error(f"Failed to cleanup agent {self.name}: {str(e)}")
            raise

    def get_status(self) -> Dict[str, Any]:
        """Get agent status information."""
        return {
            "name": self.name,
            "initialized": self._initialized,
            "uptime": (datetime.now() - self._start_time).total_seconds()
            if self._start_time else 0,
            "metrics": [m.dict() for m in self._metrics[-10:]],  # Last 10 metrics
        }

    def _record_metric(self, name: str, value: float, metadata: Optional[Dict[str, Any]] = None) -> None:
        """Record a performance metric.
        
        Args:
            name: Metric name
            value: Metric value
            metadata: Optional metadata
        """
        metric = Metric(
            name=name,
            value=value,
            metadata=metadata or {}
        )
        self._metrics.append(metric)
        
        # Keep only last 1000 metrics
        if len(self._metrics) > 1000:
            self._metrics = self._metrics[-1000:]

    @abstractmethod
    def _do_initialize(self) -> None:
        """Perform actual initialization."""
        pass

    @abstractmethod
    def _do_cleanup(self) -> None:
        """Perform actual cleanup."""
        pass


class AgentException(Exception):
    """Base exception for agent errors."""
    pass


class InitializationError(AgentException):
    """Error during agent initialization."""
    pass


class ValidationError(AgentException):
    """Error during query validation."""
    pass


class SecurityError(AgentException):
    """Security-related error."""
    pass


class ProcessingError(AgentException):
    """Error during query processing."""
    pass
