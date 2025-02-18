"""Configuration models for DBPA."""

from typing import Dict, Optional
from pydantic import BaseModel, Field, validator


class DatabaseSettings(BaseModel):
    """Database connection settings."""

    host: str = Field(..., description="Database host")
    port: int = Field(5432, gt=0, lt=65536, description="Database port")
    database: str = Field(..., min_length=1, description="Database name")
    user: str = Field(..., min_length=1, description="Database user")
    password: str = Field(..., min_length=1, description="Database password")

    class Config:
        """Pydantic model configuration."""
        frozen = True
        validate_assignment = True


class AISettings(BaseModel):
    """AI model settings."""

    model: str = Field(
        "gpt-4", 
        description="AI model name"
    )
    api_key: str = Field(
        ..., 
        min_length=1, 
        description="OpenAI API key"
    )
    temperature: float = Field(
        0.7, 
        ge=0.0, 
        le=1.0, 
        description="Model temperature"
    )
    max_tokens: int = Field(
        1000, 
        gt=0, 
        description="Maximum tokens per request"
    )
    groq_api_key: Optional[str] = Field(
        None, 
        description="Optional Groq API key"
    )

    class Config:
        """Pydantic model configuration."""
        frozen = True
        validate_assignment = True


class UISettings(BaseModel):
    """User interface settings."""

    theme: str = Field(
        "light", 
        description="UI theme (light/dark)"
    )
    language: str = Field(
        "en", 
        description="Interface language"
    )

    @validator("theme")
    def validate_theme(cls, v: str) -> str:
        """Validate theme setting.
        
        Args:
            v: Theme value
            
        Returns:
            str: Validated theme
            
        Raises:
            ValueError: If theme is invalid
        """
        if v not in ["light", "dark"]:
            raise ValueError("Theme must be 'light' or 'dark'")
        return v

    @validator("language")
    def validate_language(cls, v: str) -> str:
        """Validate language setting.
        
        Args:
            v: Language value
            
        Returns:
            str: Validated language
            
        Raises:
            ValueError: If language is invalid
        """
        if v not in ["en", "de"]:
            raise ValueError("Language must be 'en' or 'de'")
        return v

    class Config:
        """Pydantic model configuration."""
        frozen = True
        validate_assignment = True


class AppSettings(BaseModel):
    """Application settings."""

    database: DatabaseSettings = Field(
        ..., 
        description="Database settings"
    )
    ai: AISettings = Field(
        ..., 
        description="AI model settings"
    )
    ui: UISettings = Field(
        ..., 
        description="UI settings"
    )

    class Config:
        """Pydantic model configuration."""
        frozen = True
        validate_assignment = True
