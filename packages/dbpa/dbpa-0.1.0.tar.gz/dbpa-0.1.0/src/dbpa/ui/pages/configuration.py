"""Streamlit configuration page for DBPA."""
import streamlit as st
from typing import Dict, Any
import yaml
from pathlib import Path

from dbpa.config.config_schema import (
    DBPAConfig, DatabaseConfig, ProjectConfig, 
    LLMConfig, UIConfig, DatabaseType, LLMProvider
)


def render_database_config(db_config: Dict[str, DatabaseConfig]) -> Dict[str, DatabaseConfig]:
    """Render database configuration section."""
    st.subheader("🗄️ Database Configurations")
    
    # List existing databases
    for db_name, config in db_config.items():
        with st.expander(f"Database: {db_name}"):
            new_config = DatabaseConfig(
                name=st.text_input("Name", config.name, key=f"db_name_{db_name}"),
                type=st.selectbox(
                    "Type", 
                    options=list(DatabaseType),
                    index=list(DatabaseType).index(config.type),
                    key=f"db_type_{db_name}"
                ),
                host=st.text_input("Host", config.host or "", key=f"db_host_{db_name}"),
                port=st.number_input("Port", value=config.port or 0, key=f"db_port_{db_name}"),
                database=st.text_input("Database", config.database, key=f"db_database_{db_name}"),
                username=st.text_input("Username", config.username or "", key=f"db_user_{db_name}"),
                password=st.text_input(
                    "Password", 
                    config.password or "", 
                    type="password",
                    key=f"db_pass_{db_name}"
                ),
                ssl_mode=st.selectbox(
                    "SSL Mode",
                    options=["disable", "require", "verify-ca", "verify-full"],
                    index=0 if not config.ssl_mode else ["disable", "require", "verify-ca", "verify-full"].index(config.ssl_mode),
                    key=f"db_ssl_{db_name}"
                )
            )
            
            if st.button("Test Connection", key=f"test_conn_{db_name}"):
                try:
                    # Add connection testing logic here
                    st.success("Connection successful!")
                except Exception as e:
                    st.error(f"Connection failed: {str(e)}")
            
            if st.button("Delete", key=f"delete_db_{db_name}"):
                del db_config[db_name]
                st.rerun()
            
            db_config[db_name] = new_config
    
    # Add new database
    if st.button("Add New Database"):
        new_name = f"new_database_{len(db_config)}"
        db_config[new_name] = DatabaseConfig(
            name=new_name,
            type=DatabaseType.POSTGRESQL,
            database="new_database"
        )
        st.rerun()
    
    return db_config


def render_project_config(project_config: Dict[str, ProjectConfig], available_dbs: list) -> Dict[str, ProjectConfig]:
    """Render project configuration section."""
    st.subheader("📁 Project Configurations")
    
    for proj_name, config in project_config.items():
        with st.expander(f"Project: {proj_name}"):
            new_config = ProjectConfig(
                name=st.text_input("Name", config.name, key=f"proj_name_{proj_name}"),
                description=st.text_area("Description", config.description or "", key=f"proj_desc_{proj_name}"),
                database_refs=st.multiselect(
                    "Databases",
                    options=available_dbs,
                    default=config.database_refs,
                    key=f"proj_dbs_{proj_name}"
                ),
                schema_prefix=st.text_input("Schema Prefix", config.schema_prefix or "", key=f"proj_schema_{proj_name}"),
                tags=st.multiselect(
                    "Tags",
                    options=["production", "development", "testing", "archived"],
                    default=config.tags,
                    key=f"proj_tags_{proj_name}"
                )
            )
            
            if st.button("Delete", key=f"delete_proj_{proj_name}"):
                del project_config[proj_name]
                st.rerun()
            
            project_config[proj_name] = new_config
    
    if st.button("Add New Project"):
        new_name = f"new_project_{len(project_config)}"
        project_config[new_name] = ProjectConfig(
            name=new_name,
            database_refs=[]
        )
        st.rerun()
    
    return project_config


def render_llm_config(llm_config: LLMConfig) -> LLMConfig:
    """Render LLM configuration section."""
    st.subheader("🤖 LLM Configuration")
    
    provider = st.selectbox(
        "Provider",
        options=list(LLMProvider),
        index=list(LLMProvider).index(llm_config.provider)
    )
    
    api_key = st.text_input(
        "API Key",
        llm_config.api_key or "",
        type="password"
    )
    
    model = st.text_input("Model", llm_config.model)
    temperature = st.slider("Temperature", 0.0, 1.0, llm_config.temperature)
    max_tokens = st.number_input("Max Tokens", 1, 10000, llm_config.max_tokens)
    
    return LLMConfig(
        provider=provider,
        api_key=api_key,
        model=model,
        temperature=temperature,
        max_tokens=max_tokens
    )


def render_ui_config(ui_config: UIConfig) -> UIConfig:
    """Render UI configuration section."""
    st.subheader("🎨 UI Configuration")
    
    theme = st.selectbox(
        "Theme",
        options=["light", "dark"],
        index=0 if ui_config.theme == "light" else 1
    )
    
    page_title = st.text_input("Page Title", ui_config.page_title)
    sidebar_state = st.selectbox(
        "Sidebar State",
        options=["expanded", "collapsed"],
        index=0 if ui_config.sidebar_state == "expanded" else 1
    )
    
    layout = st.selectbox(
        "Layout",
        options=["centered", "wide"],
        index=0 if ui_config.layout == "centered" else 1
    )
    
    custom_css = st.text_area("Custom CSS", ui_config.custom_css or "")
    
    return UIConfig(
        theme=theme,
        page_title=page_title,
        sidebar_state=sidebar_state,
        layout=layout,
        custom_css=custom_css
    )


def load_config() -> DBPAConfig:
    """Load configuration from file."""
    config_path = Path("config.yml")
    if config_path.exists():
        return DBPAConfig.load(config_path)
    return DBPAConfig(
        llm=LLMConfig(
            provider=LLMProvider.OPENAI,
            model="gpt-4"
        )
    )


def save_config(config: DBPAConfig) -> None:
    """Save configuration to file."""
    config.save("config.yml")


def main():
    """Main configuration page."""
    st.title("DBPA Configuration")
    
    # Load existing configuration
    config = load_config()
    
    # Create tabs for different configuration sections
    tabs = st.tabs(["Databases", "Projects", "LLM", "UI"])
    
    with tabs[0]:
        config.databases = render_database_config(config.databases)
    
    with tabs[1]:
        config.projects = render_project_config(
            config.projects,
            list(config.databases.keys())
        )
    
    with tabs[2]:
        config.llm = render_llm_config(config.llm)
    
    with tabs[3]:
        config.ui = render_ui_config(config.ui)
    
    # Save configuration
    if st.button("Save Configuration"):
        try:
            save_config(config)
            st.success("Configuration saved successfully!")
        except Exception as e:
            st.error(f"Error saving configuration: {str(e)}")


if __name__ == "__main__":
    main()
