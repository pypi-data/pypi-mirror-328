"""Multilingual text-to-SQL support."""
from typing import Dict, List, Optional, Union
from pydantic import BaseModel
from pathlib import Path
import json
import yaml

class QueryTemplate(BaseModel):
    """Query template for common operations."""
    name: str
    description: Dict[str, str]  # Language code -> description
    template: str
    parameters: List[str]
    example: Dict[str, str]  # Language code -> example


class LanguageConfig(BaseModel):
    """Language-specific configuration."""
    code: str
    name: str
    date_formats: List[str]
    number_formats: Dict[str, str]
    common_phrases: Dict[str, str]
    query_templates: Dict[str, QueryTemplate]


class MultilingualSupport:
    """Multilingual support for text-to-SQL conversion."""

    def __init__(self, config_dir: Optional[str] = None):
        """Initialize multilingual support.
        
        Args:
            config_dir: Directory containing language configurations
        """
        self.config_dir = Path(config_dir) if config_dir else Path(__file__).parent / "lang_configs"
        self.languages: Dict[str, LanguageConfig] = self._load_languages()
        self.current_language = "en"

    def _load_languages(self) -> Dict[str, LanguageConfig]:
        """Load language configurations."""
        languages = {}
        for config_file in self.config_dir.glob("*.yml"):
            lang_code = config_file.stem
            with open(config_file, "r", encoding="utf-8") as f:
                config = yaml.safe_load(f)
                languages[lang_code] = LanguageConfig(**config)
        return languages

    def set_language(self, lang_code: str) -> None:
        """Set the current language."""
        if lang_code not in self.languages:
            raise ValueError(f"Language {lang_code} not supported")
        self.current_language = lang_code

    def get_query_template(self, template_name: str) -> Optional[QueryTemplate]:
        """Get a query template in the current language."""
        return self.languages[self.current_language].query_templates.get(template_name)

    def translate_common_phrase(self, phrase: str) -> str:
        """Translate a common phrase to SQL."""
        return self.languages[self.current_language].common_phrases.get(
            phrase.lower(), phrase
        )

    def format_date(self, date_str: str) -> str:
        """Format a date string according to language settings."""
        # Implementation for date formatting based on language
        pass

    def format_number(self, number_str: str) -> str:
        """Format a number string according to language settings."""
        # Implementation for number formatting based on language
        pass


# Example language configuration (German)
GERMAN_CONFIG = """
code: de
name: German
date_formats:
  - "%d.%m.%Y"
  - "%d-%m-%Y"
  - "%d/%m/%Y"
number_formats:
  decimal_separator: ","
  thousand_separator: "."
common_phrases:
  "wieviele": "COUNT"
  "anzahl der": "COUNT"
  "summe der": "SUM"
  "durchschnitt": "AVG"
  "letzte": "ORDER BY ... DESC LIMIT 1"
  "erste": "ORDER BY ... ASC LIMIT 1"
query_templates:
  count_records:
    name: count_records
    description:
      de: "Zählt die Anzahl der Datensätze in einer Tabelle"
      en: "Count records in a table"
    template: "SELECT COUNT(*) as anzahl FROM {table}"
    parameters:
      - table
    example:
      de: "Wieviele Benutzer gibt es?"
      en: "How many users are there?"
  latest_records:
    name: latest_records
    description:
      de: "Zeigt die neuesten Einträge einer Tabelle"
      en: "Show latest records from a table"
    template: >
      SELECT * FROM {table}
      ORDER BY {timestamp_column} DESC
      LIMIT {limit}
    parameters:
      - table
      - timestamp_column
      - limit
    example:
      de: "Zeige die letzten 5 Bestellungen"
      en: "Show the last 5 orders"
"""

# Example language configuration (English)
ENGLISH_CONFIG = """
code: en
name: English
date_formats:
  - "%Y-%m-%d"
  - "%m/%d/%Y"
  - "%d-%b-%Y"
number_formats:
  decimal_separator: "."
  thousand_separator: ","
common_phrases:
  "how many": "COUNT"
  "number of": "COUNT"
  "sum of": "SUM"
  "average": "AVG"
  "latest": "ORDER BY ... DESC LIMIT 1"
  "first": "ORDER BY ... ASC LIMIT 1"
query_templates:
  count_records:
    name: count_records
    description:
      en: "Count records in a table"
      de: "Zählt die Anzahl der Datensätze in einer Tabelle"
    template: "SELECT COUNT(*) as count FROM {table}"
    parameters:
      - table
    example:
      en: "How many users are there?"
      de: "Wieviele Benutzer gibt es?"
  latest_records:
    name: latest_records
    description:
      en: "Show latest records from a table"
      de: "Zeigt die neuesten Einträge einer Tabelle"
    template: >
      SELECT * FROM {table}
      ORDER BY {timestamp_column} DESC
      LIMIT {limit}
    parameters:
      - table
      - timestamp_column
      - limit
    example:
      en: "Show the last 5 orders"
      de: "Zeige die letzten 5 Bestellungen"
"""

def setup_language_configs():
    """Set up language configuration files."""
    config_dir = Path(__file__).parent / "lang_configs"
    config_dir.mkdir(exist_ok=True)
    
    # Write German config
    with open(config_dir / "de.yml", "w", encoding="utf-8") as f:
        f.write(GERMAN_CONFIG)
    
    # Write English config
    with open(config_dir / "en.yml", "w", encoding="utf-8") as f:
        f.write(ENGLISH_CONFIG)
