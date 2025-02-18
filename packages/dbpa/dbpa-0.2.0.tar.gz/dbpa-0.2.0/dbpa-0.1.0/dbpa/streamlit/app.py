"""
Main Streamlit application for DBPA.
"""
from typing import Dict, Optional
import streamlit as st
from pathlib import Path
import sys

# Add package root to Python path
root_dir = str(Path(__file__).parent.parent.parent.parent)
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from dbpa.core.config_loader import ConfigLoader
from dbpa.database.table_manager import TableManager
from dbpa.nlp.query_trainer import QueryTrainer
from dbpa.utils.error_logger import ErrorLogger


class StreamlitApp:
    """Main Streamlit application interface."""

    def __init__(self, config_path: Optional[str] = None) -> None:
        """Initialize the Streamlit application.
        
        Args:
            config_path: Optional path to config file
        """
        self.config = ConfigLoader(config_path)
        self.table_manager = TableManager()
        self.query_trainer = QueryTrainer()
        self.error_logger = ErrorLogger()
        self._setup_page_config()
        self._apply_custom_styles()

    def _setup_page_config(self) -> None:
        """Configure Streamlit page settings."""
        st.set_page_config(
            page_title="Database Personal Assistant",
            page_icon="🤖",
            layout="wide",
            initial_sidebar_state="expanded",
        )

    def _apply_custom_styles(self) -> None:
        """Apply custom CSS styles."""
        st.markdown("""
            <style>
            .stApp {
                max-width: 1200px;
                margin: 0 auto;
            }
            </style>
            """, unsafe_allow_html=True)

    def render_header(self) -> None:
        """Render the application header."""
        st.title("🤖 Database Personal Assistant")
        st.markdown("""
        Welcome to DBPA! This tool helps you interact with your database using natural language.
        Choose a tool from the sidebar to get started.
        """)

    def render_sidebar(self) -> None:
        """Render the sidebar navigation."""
        st.sidebar.title("Navigation")
        return st.sidebar.radio(
            "Choose a tool:",
            options=["Natural Language Query", "Table Manager", "Query Trainer"],
            key="navigation"
        )

    def run(self) -> None:
        """Run the Streamlit application."""
        self.render_header()
        page = self.render_sidebar()

        if page == "Natural Language Query":
            self.render_query_page()
        elif page == "Table Manager":
            self.render_table_manager()
        else:
            self.render_query_trainer()

    def render_query_page(self) -> None:
        """Render the natural language query page."""
        st.header("💬 Natural Language Query")
        query = st.text_area("Enter your query in natural language:", height=100)
        
        if st.button("Run Query"):
            if query:
                with st.spinner("Processing query..."):
                    result = self.query_trainer.generate_sql(query)
                    if result:
                        st.code(result, language="sql")
                    else:
                        st.error("Could not generate SQL query. Please try rephrasing.")
            else:
                st.warning("Please enter a query.")

    def render_table_manager(self) -> None:
        """Render the table manager page."""
        st.header("📊 Table Manager")
        available_tables = self.table_manager.get_available_tables()
        
        selected_tables = st.multiselect(
            "Select tables to manage:",
            options=available_tables,
            default=self.table_manager.selected_tables
        )

        if st.button("Save Selection"):
            self.table_manager.selected_tables = selected_tables
            st.success("Table selection saved!")

        if selected_tables:
            st.subheader("Table Details")
            for table in selected_tables:
                with st.expander(f"📋 {table}"):
                    details = self.table_manager.get_table_details(table)
                    st.dataframe(details)

    def render_query_trainer(self) -> None:
        """Render the query trainer page."""
        st.header("🎓 Query Trainer")
        example_query = st.text_area("Enter an example query:", height=100)
        expected_sql = st.text_area("Enter the expected SQL:", height=100)
        
        if st.button("Add Example"):
            if example_query and expected_sql:
                self.query_trainer.add_training_example(example_query, expected_sql)
                st.success("Training example added successfully!")
            else:
                st.warning("Please provide both the example query and expected SQL.")
