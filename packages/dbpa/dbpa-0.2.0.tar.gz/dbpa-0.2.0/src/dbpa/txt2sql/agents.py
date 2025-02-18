"""Agent-based text-to-SQL processing system."""
from typing import Dict, List, Optional, Union
from pydantic import BaseModel
from uuid import UUID, uuid4
from enum import Enum
import asyncio
import logging

from dbpa.txt2sql.engine import Txt2SQLEngine
from dbpa.txt2sql.multilingual import MultilingualSupport

logger = logging.getLogger(__name__)


class AgentType(str, Enum):
    """Types of agents in the system."""
    PARSER = "parser"
    VALIDATOR = "validator"
    OPTIMIZER = "optimizer"
    EXECUTOR = "executor"
    MONITOR = "monitor"


class AgentStatus(str, Enum):
    """Agent status states."""
    IDLE = "idle"
    BUSY = "busy"
    ERROR = "error"


class AgentPriority(int, Enum):
    """Agent priority levels."""
    LOW = 1
    MEDIUM = 2
    HIGH = 3


class ResourceLimits(BaseModel):
    """Resource limits for agents."""
    max_memory: str
    max_cpu: float
    max_tasks: int


class AgentConfig(BaseModel):
    """Agent configuration."""
    agent_type: AgentType
    priority: AgentPriority
    resource_limits: ResourceLimits


class AgentMessage(BaseModel):
    """Message passed between agents."""
    id: UUID = None
    sender: str
    receiver: str
    content: Dict
    priority: AgentPriority
    timestamp: float

    def __init__(self, **data):
        super().__init__(**data)
        if self.id is None:
            self.id = uuid4()


class SQLAgent:
    """Base class for SQL processing agents."""

    def __init__(
        self,
        name: str,
        config: AgentConfig,
        engine: Txt2SQLEngine,
        multilingual: MultilingualSupport
    ):
        """Initialize the agent."""
        self.name = name
        self.config = config
        self.engine = engine
        self.multilingual = multilingual
        self.status = AgentStatus.IDLE
        self.message_queue: asyncio.Queue = asyncio.Queue()
        self.results: Dict[UUID, Dict] = {}

    async def process_message(self, message: AgentMessage) -> Optional[AgentMessage]:
        """Process an incoming message."""
        raise NotImplementedError

    async def run(self):
        """Run the agent's main loop."""
        while True:
            try:
                message = await self.message_queue.get()
                self.status = AgentStatus.BUSY
                result = await self.process_message(message)
                if result:
                    self.results[result.id] = result.content
                self.status = AgentStatus.IDLE
            except Exception as e:
                logger.error(f"Error in agent {self.name}: {str(e)}")
                self.status = AgentStatus.ERROR


class ParserAgent(SQLAgent):
    """Agent for parsing natural language queries."""

    async def process_message(self, message: AgentMessage) -> Optional[AgentMessage]:
        """Parse natural language query into initial SQL."""
        query = message.content["query"]
        language = message.content.get("language", "en")
        
        # Set language for processing
        self.multilingual.set_language(language)
        
        # Check for common phrases and templates
        template = self.multilingual.get_query_template(query)
        if template:
            sql = template.template.format(**message.content.get("parameters", {}))
        else:
            # Generate SQL using the engine
            sql = self.engine.generate_query(query)
        
        return AgentMessage(
            sender=self.name,
            receiver="validator",
            content={"sql": sql, "original_query": query},
            priority=message.priority
        )


class ValidatorAgent(SQLAgent):
    """Agent for validating and correcting SQL queries."""

    async def process_message(self, message: AgentMessage) -> Optional[AgentMessage]:
        """Validate and potentially correct SQL query."""
        sql = message.content["sql"]
        try:
            # Validate SQL syntax and schema
            valid = self.engine.validate_query(sql)
            if not valid:
                # Try to correct the query
                sql = self.engine.correct_query(sql)
            
            return AgentMessage(
                sender=self.name,
                receiver="optimizer",
                content={
                    "sql": sql,
                    "original_query": message.content["original_query"],
                    "validation": "success"
                },
                priority=message.priority
            )
        except Exception as e:
            return AgentMessage(
                sender=self.name,
                receiver="parser",
                content={
                    "error": str(e),
                    "original_query": message.content["original_query"]
                },
                priority=message.priority
            )


class OptimizerAgent(SQLAgent):
    """Agent for optimizing SQL queries."""

    async def process_message(self, message: AgentMessage) -> Optional[AgentMessage]:
        """Optimize SQL query for better performance."""
        sql = message.content["sql"]
        try:
            # Get query execution plan
            plan = self.engine.explain_query(sql)
            
            # Optimize if needed
            if self._needs_optimization(plan):
                sql = self.engine.optimize_query(sql)
            
            return AgentMessage(
                sender=self.name,
                receiver="executor",
                content={
                    "sql": sql,
                    "original_query": message.content["original_query"],
                    "execution_plan": plan
                },
                priority=message.priority
            )
        except Exception as e:
            logger.error(f"Optimization error: {str(e)}")
            # Forward the original SQL if optimization fails
            return AgentMessage(
                sender=self.name,
                receiver="executor",
                content=message.content,
                priority=message.priority
            )

    def _needs_optimization(self, plan: str) -> bool:
        """Check if query needs optimization based on execution plan."""
        # Implementation for checking execution plan
        return False


class ExecutorAgent(SQLAgent):
    """Agent for executing SQL queries."""

    async def process_message(self, message: AgentMessage) -> Optional[AgentMessage]:
        """Execute SQL query and return results."""
        sql = message.content["sql"]
        try:
            result = self.engine.execute_query(sql)
            return AgentMessage(
                sender=self.name,
                receiver="monitor",
                content={
                    "sql": sql,
                    "original_query": message.content["original_query"],
                    "result": result.dict(),
                    "execution_plan": message.content.get("execution_plan")
                },
                priority=message.priority
            )
        except Exception as e:
            return AgentMessage(
                sender=self.name,
                receiver="monitor",
                content={
                    "sql": sql,
                    "original_query": message.content["original_query"],
                    "error": str(e)
                },
                priority=message.priority
            )


class MonitorAgent(SQLAgent):
    """Agent for monitoring and logging query execution."""

    async def process_message(self, message: AgentMessage) -> Optional[AgentMessage]:
        """Monitor query execution and log results."""
        content = message.content
        
        # Log query execution
        if "error" in content:
            logger.error(f"Query execution failed: {content['error']}")
            logger.error(f"SQL: {content['sql']}")
            logger.error(f"Original query: {content['original_query']}")
        else:
            logger.info(f"Query executed successfully: {content['sql']}")
            logger.info(f"Original query: {content['original_query']}")
            logger.info(f"Execution time: {content['result']['execution_time']}s")
            
            if "execution_plan" in content:
                logger.debug(f"Execution plan: {content['execution_plan']}")
        
        return None  # Monitor is the final agent in the chain
