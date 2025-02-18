"""Streamlit components for vector store management."""
from typing import Dict, Any, Optional, List, Tuple
import streamlit as st
from datetime import datetime
import pandas as pd

from dbpa.txt2sql.models.examples import QueryExample
from dbpa.txt2sql.agents.data_management_agent import DataManagementAgent, QueryEdit


def render_add_query_form() -> Dict[str, Any]:
    """Render form for adding new query pairs."""
    with st.form("add_query_form"):
        natural_query = st.text_area(
            "Natural Language Query",
            placeholder="Enter the natural language query..."
        )
        sql_query = st.text_area(
            "SQL Query",
            placeholder="Enter the corresponding SQL query..."
        )
        language = st.selectbox(
            "Language",
            options=["en", "de"],
            help="Select the query language"
        )
        database_type = st.selectbox(
            "Database Type",
            options=["postgresql", "mysql", "sqlite"],
            help="Select the database type"
        )
        schema_hash = st.text_input(
            "Schema Hash",
            placeholder="Enter the schema hash..."
        )
        
        # Metadata as key-value pairs
        st.subheader("Metadata (Optional)")
        num_metadata = st.number_input(
            "Number of metadata fields",
            min_value=0,
            max_value=10,
            value=0
        )
        
        metadata = {}
        for i in range(num_metadata):
            col1, col2 = st.columns(2)
            key = col1.text_input(f"Key {i+1}")
            value = col2.text_input(f"Value {i+1}")
            if key and value:
                metadata[key] = value
        
        submitted = st.form_submit_button("Add Query Pair")
        
        if submitted:
            return {
                "natural_query": natural_query,
                "sql_query": sql_query,
                "language": language,
                "database_type": database_type,
                "schema_hash": schema_hash,
                "metadata": metadata
            }
    return {}


def render_query_table(
    examples: Dict[int, QueryExample],
    deleted: bool = False
) -> None:
    """Render table of query examples."""
    if not examples:
        st.info("No examples found." if not deleted else "No deleted examples found.")
        return

    # Convert to DataFrame for better display
    data = []
    for idx, example in examples.items():
        row = {
            "ID": idx,
            "Natural Query": example.natural_query,
            "SQL Query": example.sql_query,
            "Language": example.language,
            "Database": example.database_type,
            "Success Rate": f"{example.success_rate:.2%}",
            "Usage Count": example.usage_count,
            "Last Used": example.last_used.strftime("%Y-%m-%d %H:%M")
        }
        data.append(row)
    
    df = pd.DataFrame(data)
    st.dataframe(
        df,
        column_config={
            "ID": st.column_config.NumberColumn(
                "ID",
                help="Example ID"
            ),
            "Natural Query": st.column_config.TextColumn(
                "Natural Query",
                help="Natural language query",
                width="large"
            ),
            "SQL Query": st.column_config.TextColumn(
                "SQL Query",
                help="SQL query",
                width="large"
            )
        },
        hide_index=True
    )


def render_edit_form(example: QueryExample) -> Optional[QueryEdit]:
    """Render form for editing a query example."""
    with st.form("edit_form"):
        natural_query = st.text_area(
            "Natural Language Query",
            value=example.natural_query
        )
        sql_query = st.text_area(
            "SQL Query",
            value=example.sql_query
        )
        
        # Metadata editor
        st.subheader("Metadata")
        metadata = dict(example.metadata)
        
        # Existing metadata
        to_delete = []
        for key, value in metadata.items():
            col1, col2, col3 = st.columns([2, 2, 1])
            new_key = col1.text_input(f"Key", value=key, key=f"key_{key}")
            new_value = col2.text_input(f"Value", value=value, key=f"value_{key}")
            if col3.button("Delete", key=f"delete_{key}"):
                to_delete.append(key)
            
            if new_key != key:
                metadata[new_key] = metadata.pop(key)
            if new_value != value:
                metadata[key] = new_value
                
        for key in to_delete:
            metadata.pop(key)
            
        # New metadata
        if st.button("Add Metadata Field"):
            metadata["new_key"] = "new_value"
            
        submitted = st.form_submit_button("Save Changes")
        
        if submitted:
            edits = QueryEdit(
                natural_query=natural_query if natural_query != example.natural_query else None,
                sql_query=sql_query if sql_query != example.sql_query else None,
                metadata=metadata if metadata != example.metadata else None
            )
            return edits
    return None


def render_deleted_examples_table(
    examples: Dict[int, Tuple[QueryExample, datetime]]
) -> None:
    """Render table of deleted examples."""
    if not examples:
        st.info("No deleted examples found.")
        return

    data = []
    for idx, (example, deleted_at) in examples.items():
        row = {
            "ID": idx,
            "Natural Query": example.natural_query,
            "SQL Query": example.sql_query,
            "Language": example.language,
            "Database": example.database_type,
            "Deleted At": deleted_at.strftime("%Y-%m-%d %H:%M"),
            "Success Rate": f"{example.success_rate:.2%}",
            "Usage Count": example.usage_count
        }
        data.append(row)
    
    df = pd.DataFrame(data)
    st.dataframe(
        df,
        column_config={
            "ID": st.column_config.NumberColumn(
                "ID",
                help="Example ID"
            ),
            "Natural Query": st.column_config.TextColumn(
                "Natural Query",
                help="Natural language query",
                width="large"
            ),
            "SQL Query": st.column_config.TextColumn(
                "SQL Query",
                help="SQL query",
                width="large"
            ),
            "Deleted At": st.column_config.DatetimeColumn(
                "Deleted At",
                help="When the example was deleted",
                format="DD/MM/YY HH:mm"
            )
        },
        hide_index=True
    )
