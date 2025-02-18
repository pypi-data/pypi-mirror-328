"""Error logging functionality for DBPA."""

import logging
from pathlib import Path
from datetime import datetime
from typing import Optional


class ErrorLogger:
    """Handles error logging for the application."""

    def __init__(self, log_file: Optional[str] = None) -> None:
        """Initialize the error logger.
        
        Args:
            log_file: Optional path to log file
        """
        if not log_file:
            log_dir = Path(__file__).parent.parent.parent.parent / "logs"
            log_dir.mkdir(exist_ok=True)
            log_file = str(log_dir / "error.log")

        self.logger = logging.getLogger("dbpa")
        self.logger.setLevel(logging.ERROR)

        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

    def log_error(self, message: str) -> None:
        """Log an error message.
        
        Args:
            message: Error message to log
        """
        self.logger.error(message)
