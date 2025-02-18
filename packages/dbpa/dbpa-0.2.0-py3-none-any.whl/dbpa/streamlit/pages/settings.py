"""
Settings Page - Configure DBPA settings.
"""
import streamlit as st
from pathlib import Path
import sys
from typing import Dict, Any

# Add package root to Python path
root_dir = str(Path(__file__).parent.parent.parent.parent.parent)
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from dbpa.core.config_loader import ConfigLoader


def render_settings() -> None:
    """Render the settings page."""
    st.set_page_config(page_title="Settings - DBPA", page_icon="⚙️")
    st.title("⚙️ Settings")

    config = ConfigLoader()
    settings = config.load_settings()

    # Database Settings
    st.header("Database Settings")
    db_settings = settings.get("database", {})
    
    col1, col2 = st.columns(2)
    with col1:
        host = st.text_input("Host", value=db_settings.get("host", ""))
        database = st.text_input("Database", value=db_settings.get("database", ""))
        port = st.number_input("Port", value=int(db_settings.get("port", 5432)))
    
    with col2:
        user = st.text_input("User", value=db_settings.get("user", ""))
        password = st.text_input("Password", value=db_settings.get("password", ""), type="password")

    # AI Model Settings
    st.header("AI Model Settings")
    ai_settings = settings.get("ai", {})
    
    model = st.selectbox(
        "Model",
        options=["gpt-4", "gpt-3.5-turbo", "groq-mixtral"],
        index=["gpt-4", "gpt-3.5-turbo", "groq-mixtral"].index(
            ai_settings.get("model", "gpt-4")
        )
    )
    
    temperature = st.slider(
        "Temperature",
        min_value=0.0,
        max_value=1.0,
        value=float(ai_settings.get("temperature", 0.7)),
        step=0.1
    )
    
    max_tokens = st.number_input(
        "Max Tokens",
        min_value=100,
        max_value=4000,
        value=int(ai_settings.get("max_tokens", 1000))
    )

    # UI Settings
    st.header("UI Settings")
    ui_settings = settings.get("ui", {})
    
    theme = st.selectbox(
        "Theme",
        options=["light", "dark"],
        index=["light", "dark"].index(ui_settings.get("theme", "light"))
    )
    
    language = st.selectbox(
        "Language",
        options=["English", "German"],
        index=["en", "de"].index(ui_settings.get("language", "en"))
    )

    # Save Settings
    if st.button("Save Settings"):
        new_settings: Dict[str, Any] = {
            "database": {
                "host": host,
                "database": database,
                "port": port,
                "user": user,
                "password": password
            },
            "ai": {
                "model": model,
                "temperature": temperature,
                "max_tokens": max_tokens
            },
            "ui": {
                "theme": theme,
                "language": "en" if language == "English" else "de"
            }
        }
        
        if config.save_settings(new_settings):
            st.success("Settings saved successfully!")
        else:
            st.error("Error saving settings. Please try again.")

    # Reset Settings
    if st.button("Reset to Defaults"):
        if config.reset_settings():
            st.success("Settings reset to defaults!")
            st.experimental_rerun()
        else:
            st.error("Error resetting settings. Please try again.")


if __name__ == "__main__":
    render_settings()
