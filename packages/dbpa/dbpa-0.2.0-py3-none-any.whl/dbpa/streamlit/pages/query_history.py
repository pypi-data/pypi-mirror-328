"""
Query History Page - View and analyze past queries.
"""
import streamlit as st
from pathlib import Path
import sys
from typing import List, Dict
import pandas as pd

# Add package root to Python path
root_dir = str(Path(__file__).parent.parent.parent.parent.parent)
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from dbpa.nlp.query_trainer import QueryTrainer


def format_query_history(history: List[Dict]) -> pd.DataFrame:
    """Format query history into a DataFrame.
    
    Args:
        history: List of query history entries
        
    Returns:
        pd.DataFrame: Formatted history
    """
    if not history:
        return pd.DataFrame()
        
    df = pd.DataFrame(history)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df = df.sort_values("timestamp", ascending=False)
    return df[["timestamp", "natural_query", "sql_query", "success"]]


def render_query_history() -> None:
    """Render the query history page."""
    st.set_page_config(page_title="Query History - DBPA", page_icon="📜")
    st.title("📜 Query History")

    trainer = QueryTrainer()
    history = trainer.get_query_history()
    
    # Filter options
    st.sidebar.header("Filters")
    success_filter = st.sidebar.multiselect(
        "Status",
        options=["Success", "Failed"],
        default=["Success", "Failed"]
    )
    
    date_range = st.sidebar.date_input(
        "Date Range",
        value=(pd.Timestamp.now() - pd.Timedelta(days=7), pd.Timestamp.now())
    )

    # Format and filter history
    df = format_query_history(history)
    if not df.empty:
        # Apply filters
        mask = df["success"].isin([s.lower() == "success" for s in success_filter])
        if isinstance(date_range, tuple):
            start_date, end_date = date_range
            mask &= (df["timestamp"].dt.date >= start_date) & (df["timestamp"].dt.date <= end_date)
        
        filtered_df = df[mask]
        
        # Display statistics
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Queries", len(filtered_df))
        with col2:
            success_rate = (filtered_df["success"].sum() / len(filtered_df)) * 100
            st.metric("Success Rate", f"{success_rate:.1f}%")
        with col3:
            st.metric("Unique Patterns", len(filtered_df["natural_query"].unique()))

        # Display history table
        st.dataframe(
            filtered_df.style.apply(
                lambda x: ["background: #e6ffe6" if v else "background: #ffe6e6" 
                         for v in x["success"]], axis=1
            )
        )

        # Download option
        if st.button("Download History"):
            csv = filtered_df.to_csv(index=False)
            st.download_button(
                "Click to Download",
                csv,
                "query_history.csv",
                "text/csv",
                key="download-csv"
            )
    else:
        st.info("No query history available.")


if __name__ == "__main__":
    render_query_history()
