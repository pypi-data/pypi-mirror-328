"""Configuration loading functionality for DBPA."""

import json
import os
from pathlib import Path
from typing import Any, Dict, Optional
from dotenv import load_dotenv

from dbpa.utils.error_logger import ErrorLogger
from dbpa.models.config import (
    AppSettings,
    DatabaseSettings,
    AISettings,
    UISettings
)


class ConfigLoader:
    """Handles loading and saving of application configuration."""

    def __init__(self, config_path: Optional[str] = None) -> None:
        """Initialize the config loader.
        
        Args:
            config_path: Optional path to config file
        """
        self.error_logger = ErrorLogger()
        
        if not config_path:
            config_dir = Path(__file__).parent.parent.parent.parent / "config"
            config_dir.mkdir(exist_ok=True)
            self.config_path = config_dir / "settings.json"
        else:
            self.config_path = Path(config_path)

        self._ensure_config_exists()

    def _ensure_config_exists(self) -> None:
        """Ensure config file exists with default settings."""
        if not self.config_path.exists():
            # Load environment variables
            env_path = Path(__file__).parent.parent.parent.parent / ".env"
            load_dotenv(env_path)
            
            try:
                # Create settings using Pydantic models
                db_settings = DatabaseSettings(
                    host=os.getenv("POSTGRES_HOST", "localhost"),
                    port=int(os.getenv("POSTGRES_PORT", "5432")),
                    database=os.getenv("POSTGRES_DATABASE", ""),
                    user=os.getenv("POSTGRES_USER", ""),
                    password=os.getenv("POSTGRES_PASSWORD", "")
                )

                ai_settings = AISettings(
                    model=os.getenv("OPENAI_MODEL_NAME", "gpt-4"),
                    api_key=os.getenv("OPENAI_API_KEY", ""),
                    temperature=0.7,
                    max_tokens=1000,
                    groq_api_key=os.getenv("GROQ_API_KEY")
                )

                ui_settings = UISettings(
                    theme="light",
                    language="en"
                )

                app_settings = AppSettings(
                    database=db_settings,
                    ai=ai_settings,
                    ui=ui_settings
                )

                # Save validated settings
                self.save_settings(app_settings.dict())
                
            except Exception as e:
                self.error_logger.log_error(f"Error creating default settings: {str(e)}")
                raise

    def load_settings(self) -> Dict[str, Any]:
        """Load settings from config file.
        
        Returns:
            Dict[str, Any]: Configuration settings
        """
        try:
            with open(self.config_path, "r") as f:
                data = json.load(f)
                # Validate settings using Pydantic
                AppSettings(**data)
                return data
        except Exception as e:
            self.error_logger.log_error(f"Error loading settings: {str(e)}")
            return {}

    def save_settings(self, settings: Dict[str, Any]) -> bool:
        """Save settings to config file.
        
        Args:
            settings: Configuration settings to save
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # Validate settings using Pydantic
            AppSettings(**settings)
            
            with open(self.config_path, "w") as f:
                json.dump(settings, f, indent=4)
            return True
        except Exception as e:
            self.error_logger.log_error(f"Error saving settings: {str(e)}")
            return False

    def reset_settings(self) -> bool:
        """Reset settings to defaults.
        
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            if self.config_path.exists():
                self.config_path.unlink()
            self._ensure_config_exists()
            return True
        except Exception as e:
            self.error_logger.log_error(f"Error resetting settings: {str(e)}")
            return False
