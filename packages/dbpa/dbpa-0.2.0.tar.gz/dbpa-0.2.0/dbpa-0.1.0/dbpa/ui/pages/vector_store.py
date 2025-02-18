"""Vector store management page."""
import streamlit as st
from pathlib import Path
import logging
from datetime import datetime

from dbpa.txt2sql.vector_store.store import VectorStore
from dbpa.txt2sql.agents.data_management_agent import DataManagementAgent
from dbpa.ui.components import vector_store_manager as vsm

logger = logging.getLogger(__name__)


def initialize_vector_store() -> VectorStore:
    """Initialize or load vector store."""
    store_dir = Path("data/vector_store")
    store_dir.mkdir(parents=True, exist_ok=True)
    
    if (store_dir / "index.faiss").exists():
        return VectorStore.load(store_dir)
    return VectorStore()


def initialize_agent() -> DataManagementAgent:
    """Initialize data management agent."""
    if "vector_store" not in st.session_state:
        st.session_state.vector_store = initialize_vector_store()
        
    backup_dir = Path("data/backups")
    return DataManagementAgent(
        vector_store=st.session_state.vector_store,
        backup_dir=backup_dir,
        max_backup_count=10
    )


def render_page() -> None:
    """Render vector store management page."""
    st.title("Vector Store Management")
    
    # Initialize agent
    agent = initialize_agent()
    
    # Tabs for different operations
    tab_main, tab_deleted = st.tabs(["Main", "Deleted Examples"])
    
    with tab_main:
        # Top section: Add new query pair
        st.header("Add New Query Pair")
        add_data = vsm.render_add_query_form()
        if add_data:
            try:
                example_id = agent.add_query_pair(**add_data)
                st.success(f"Successfully added query pair with ID: {example_id}")
            except Exception as e:
                st.error(f"Error adding query pair: {str(e)}")
                logger.exception("Error adding query pair")
        
        # Middle section: View and manage existing examples
        st.header("Existing Query Examples")
        
        # Search and filter
        col1, col2 = st.columns(2)
        with col1:
            search_query = st.text_input(
                "Search Natural Query",
                placeholder="Enter text to filter..."
            )
        with col2:
            language_filter = st.selectbox(
                "Filter by Language",
                options=["All", "en", "de"]
            )
        
        # Get and filter examples
        examples = {
            k: v for k, v in agent._store._examples.items()
            if (not search_query or search_query.lower() in v.natural_query.lower()) and
            (language_filter == "All" or v.language == language_filter)
        }
        
        vsm.render_query_table(examples)
        
        # Example management
        if examples:
            st.subheader("Manage Example")
            example_id = st.number_input(
                "Example ID",
                min_value=min(examples.keys()),
                max_value=max(examples.keys())
            )
            
            if example_id in examples:
                example = examples[example_id]
                
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("Edit Example"):
                        st.session_state.editing_example = example_id
                with col2:
                    if st.button("Delete Example"):
                        if agent.delete_query_pair(example_id):
                            st.success(f"Deleted example {example_id}")
                        else:
                            st.error(f"Failed to delete example {example_id}")
                
                # Edit form
                if getattr(st.session_state, "editing_example", None) == example_id:
                    st.subheader(f"Edit Example {example_id}")
                    edits = vsm.render_edit_form(example)
                    if edits:
                        if agent.edit_query_pair(example_id, edits):
                            st.success("Successfully updated example")
                            st.session_state.editing_example = None
                        else:
                            st.error("Failed to update example")
    
    with tab_deleted:
        st.header("Deleted Examples")
        
        # Filter options
        max_age = st.slider(
            "Maximum Age (days)",
            min_value=1,
            max_value=30,
            value=7
        )
        
        # Get and display deleted examples
        deleted_examples = agent.get_deleted_examples(max_age_days=max_age)
        vsm.render_deleted_examples_table(deleted_examples)
        
        # Restore functionality
        if deleted_examples:
            st.subheader("Restore Example")
            restore_id = st.number_input(
                "Example ID to Restore",
                min_value=min(deleted_examples.keys()),
                max_value=max(deleted_examples.keys())
            )
            
            if st.button("Restore Example"):
                if agent.restore_query_pair(restore_id):
                    st.success(f"Restored example {restore_id}")
                else:
                    st.error(f"Failed to restore example {restore_id}")
        
        # Cleanup option
        if st.button("Cleanup Old Deleted Examples"):
            removed = agent.cleanup_deleted_examples(max_age)
            st.info(f"Removed {removed} old deleted examples")


if __name__ == "__main__":
    render_page()
