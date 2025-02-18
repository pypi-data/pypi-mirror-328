"""
Table Details Page - Detailed view of database table information.
"""
import streamlit as st
from pathlib import Path
import sys

# Add package root to Python path
root_dir = str(Path(__file__).parent.parent.parent.parent.parent)
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from dbpa.database.table_manager import TableManager


def render_table_details() -> None:
    """Render the table details page."""
    st.set_page_config(page_title="Table Details - DBPA", page_icon="📋")
    st.title("📋 Table Details")

    manager = TableManager()
    table_name = st.experimental_get_query_params().get("table", [None])[0]

    if not table_name:
        st.warning("Please select a table from the Table Manager.")
        return

    details = manager.get_table_details(table_name)
    if not details.empty:
        st.header(f"Table: {table_name}")
        
        # Display table statistics
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Total Columns", len(details))
        with col2:
            st.metric("Total Rows", manager.get_row_count(table_name))

        # Display column details
        st.subheader("Column Information")
        st.dataframe(
            details.style.set_properties(**{
                "background-color": "lightgray",
                "color": "black",
                "border-color": "white"
            })
        )

        # Display sample data
        st.subheader("Sample Data")
        sample_data = manager.get_sample_data(table_name)
        if not sample_data.empty:
            st.dataframe(sample_data)
        else:
            st.info("No sample data available.")

        # Display relationships
        st.subheader("Table Relationships")
        relationships = manager.get_table_relationships(table_name)
        if relationships:
            for rel in relationships:
                st.markdown(f"- {rel}")
        else:
            st.info("No relationships found.")
    else:
        st.error(f"Could not fetch details for table {table_name}")


if __name__ == "__main__":
    render_table_details()
