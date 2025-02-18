"""Configuration schema for DBPA framework."""
from typing import Dict, List, Optional, Union
from pydantic import BaseModel, Field, validator
from enum import Enum
import json
import yaml
from pathlib import Path


class DatabaseType(str, Enum):
    """Supported database types."""
    POSTGRESQL = "postgresql"
    MYSQL = "mysql"
    MSSQL = "mssql"
    ORACLE = "oracle"
    SQLITE = "sqlite"
    SNOWFLAKE = "snowflake"
    BIGQUERY = "bigquery"


class LLMProvider(str, Enum):
    """Supported LLM providers."""
    OPENAI = "openai"
    GROQ = "groq"
    ANTHROPIC = "anthropic"
    AZURE = "azure_openai"
    LOCAL = "local"


class DatabaseConfig(BaseModel):
    """Database connection configuration."""
    name: str = Field(..., description="Unique name for this database connection")
    type: DatabaseType = Field(..., description="Type of database")
    host: Optional[str] = Field(None, description="Database host")
    port: Optional[int] = Field(None, description="Database port")
    database: str = Field(..., description="Database name")
    username: Optional[str] = Field(None, description="Database username")
    password: Optional[str] = Field(None, description="Database password")
    connection_string: Optional[str] = Field(None, description="Full connection string (if needed)")
    ssl_mode: Optional[str] = Field(None, description="SSL mode for connection")
    options: Dict[str, str] = Field(default_factory=dict, description="Additional connection options")

    class Config:
        protected_fields = {"password"}


class ProjectConfig(BaseModel):
    """Project-specific configuration."""
    name: str = Field(..., description="Project name")
    description: Optional[str] = Field(None, description="Project description")
    database_refs: List[str] = Field(..., description="References to database configurations")
    schema_prefix: Optional[str] = Field(None, description="Prefix for all schemas in this project")
    tags: List[str] = Field(default_factory=list, description="Project tags")
    metadata: Dict[str, str] = Field(default_factory=dict, description="Additional project metadata")


class LLMConfig(BaseModel):
    """LLM provider configuration."""
    provider: LLMProvider = Field(..., description="LLM provider")
    api_key: Optional[str] = Field(None, description="API key for the provider")
    model: str = Field(..., description="Model name/version")
    temperature: float = Field(0.7, description="Model temperature")
    max_tokens: int = Field(2000, description="Maximum tokens per request")
    options: Dict[str, str] = Field(default_factory=dict, description="Additional provider options")

    class Config:
        protected_fields = {"api_key"}


class UIConfig(BaseModel):
    """Streamlit UI configuration."""
    theme: str = Field("light", description="UI theme (light/dark)")
    page_title: str = Field("DBPA", description="Page title")
    sidebar_state: str = Field("expanded", description="Initial sidebar state")
    layout: str = Field("wide", description="Page layout")
    custom_css: Optional[str] = Field(None, description="Custom CSS")


class DBPAConfig(BaseModel):
    """Main DBPA configuration."""
    version: str = Field("1.0.0", description="Configuration version")
    databases: Dict[str, DatabaseConfig] = Field(
        default_factory=dict, 
        description="Database configurations"
    )
    projects: Dict[str, ProjectConfig] = Field(
        default_factory=dict,
        description="Project configurations"
    )
    llm: LLMConfig = Field(..., description="LLM configuration")
    ui: UIConfig = Field(default_factory=UIConfig, description="UI configuration")
    logging: Dict[str, str] = Field(
        default_factory=lambda: {
            "level": "INFO",
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        }
    )

    @validator("projects")
    def validate_database_refs(cls, v, values):
        """Ensure all database references exist."""
        if "databases" in values:
            for project in v.values():
                for db_ref in project.database_refs:
                    if db_ref not in values["databases"]:
                        raise ValueError(f"Database reference '{db_ref}' not found")
        return v

    def save(self, path: Union[str, Path]) -> None:
        """Save configuration to file."""
        path = Path(path)
        if path.suffix == ".json":
            path.write_text(self.json(indent=2, exclude=self.get_protected_fields()))
        elif path.suffix in {".yml", ".yaml"}:
            path.write_text(yaml.dump(
                json.loads(self.json(exclude=self.get_protected_fields())),
                default_flow_style=False
            ))
        else:
            raise ValueError("Unsupported file format. Use .json, .yml, or .yaml")

    @classmethod
    def load(cls, path: Union[str, Path]) -> "DBPAConfig":
        """Load configuration from file."""
        path = Path(path)
        if not path.exists():
            raise FileNotFoundError(f"Configuration file not found: {path}")
        
        if path.suffix == ".json":
            return cls.parse_file(path)
        elif path.suffix in {".yml", ".yaml"}:
            return cls.parse_obj(yaml.safe_load(path.read_text()))
        else:
            raise ValueError("Unsupported file format. Use .json, .yml, or .yaml")

    def get_protected_fields(self) -> set:
        """Get all protected fields that should not be saved to file."""
        protected = set()
        for db in self.databases.values():
            protected.update({f"databases.{db.name}.{f}" 
                            for f in db.Config.protected_fields})
        protected.update({f"llm.{f}" 
                         for f in self.llm.Config.protected_fields})
        return protected
