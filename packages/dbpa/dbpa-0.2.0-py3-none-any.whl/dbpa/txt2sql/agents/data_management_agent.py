"""Agent for managing vector store data and query examples."""
from typing import Dict, List, Optional, Any, Tuple
import logging
from datetime import datetime
from pathlib import Path
import json

from pydantic import BaseModel, Field, ConfigDict
from dbpa.txt2sql.models.examples import QueryExample
from dbpa.txt2sql.vector_store.store import VectorStore

logger = logging.getLogger(__name__)


class QueryEdit(BaseModel):
    """Model for query example edits."""
    natural_query: Optional[str] = Field(None, description="Updated natural language query")
    sql_query: Optional[str] = Field(None, description="Updated SQL query")
    metadata: Optional[Dict[str, Any]] = Field(None, description="Updated metadata")

    model_config = ConfigDict(
        validate_assignment=True,
        extra="forbid"
    )


class DataManagementAgent:
    """Agent for managing vector store data and query examples."""

    def __init__(
        self,
        vector_store: VectorStore,
        backup_dir: Optional[Path] = None,
        max_backup_count: int = 5
    ):
        """Initialize data management agent.
        
        Args:
            vector_store: Vector store instance
            backup_dir: Optional directory for backups
            max_backup_count: Maximum number of backups to keep
        """
        self._store = vector_store
        self._backup_dir = Path(backup_dir) if backup_dir else None
        self._max_backup_count = max_backup_count
        self._deleted_examples: Dict[int, Tuple[QueryExample, datetime]] = {}

    def add_query_pair(
        self,
        natural_query: str,
        sql_query: str,
        language: str,
        database_type: str,
        schema_hash: str,
        metadata: Optional[Dict[str, Any]] = None,
        create_backup: bool = True
    ) -> int:
        """Add a new query example pair.
        
        Args:
            natural_query: Natural language query
            sql_query: Generated SQL query
            language: Language code
            database_type: Database type
            schema_hash: Schema hash
            metadata: Optional metadata
            create_backup: Whether to create a backup
            
        Returns:
            ID of the new example
        """
        if create_backup:
            self._create_backup("pre_add")

        example = QueryExample(
            natural_query=natural_query,
            sql_query=sql_query,
            language=language,
            database_type=database_type,
            schema_hash=schema_hash,
            metadata=metadata or {}
        )
        
        example_id = self._store.add_example(example)
        logger.info(f"Added new query example with ID {example_id}")
        return example_id

    def edit_query_pair(
        self,
        example_id: int,
        edits: QueryEdit,
        create_backup: bool = True
    ) -> bool:
        """Edit an existing query example.
        
        Args:
            example_id: ID of example to edit
            edits: Changes to apply
            create_backup: Whether to create a backup
            
        Returns:
            True if successful, False if example not found
        """
        if example_id not in self._store._examples:
            logger.warning(f"Example {example_id} not found")
            return False

        if create_backup:
            self._create_backup(f"pre_edit_{example_id}")

        example = self._store._examples[example_id]
        
        if edits.natural_query is not None:
            example.natural_query = edits.natural_query
            # Recompute embedding
            example.embedding = self._store._compute_embedding(edits.natural_query)
            
        if edits.sql_query is not None:
            example.sql_query = edits.sql_query
            
        if edits.metadata is not None:
            example.metadata.update(edits.metadata)

        # Update FAISS index
        if edits.natural_query is not None:
            self._store._index.remove_ids(example_id)
            self._store._index.add(self._store._to_numpy_array([example.embedding]))

        logger.info(f"Updated example {example_id}")
        return True

    def delete_query_pair(
        self,
        example_id: int,
        create_backup: bool = True,
        soft_delete: bool = True
    ) -> bool:
        """Delete a query example.
        
        Args:
            example_id: ID of example to delete
            create_backup: Whether to create a backup
            soft_delete: If True, keep example in deleted items history
            
        Returns:
            True if successful, False if example not found
        """
        if example_id not in self._store._examples:
            logger.warning(f"Example {example_id} not found")
            return False

        if create_backup:
            self._create_backup(f"pre_delete_{example_id}")

        example = self._store._examples[example_id]
        
        if soft_delete:
            self._deleted_examples[example_id] = (example, datetime.now())
            
        del self._store._examples[example_id]
        self._store._index.remove_ids(example_id)
        
        logger.info(f"Deleted example {example_id}")
        return True

    def restore_query_pair(self, example_id: int) -> bool:
        """Restore a previously deleted query example.
        
        Args:
            example_id: ID of example to restore
            
        Returns:
            True if successful, False if example not found in deleted items
        """
        if example_id not in self._deleted_examples:
            logger.warning(f"Deleted example {example_id} not found")
            return False

        example, _ = self._deleted_examples[example_id]
        self._store._examples[example_id] = example
        self._store._index.add(self._store._to_numpy_array([example.embedding]))
        
        del self._deleted_examples[example_id]
        logger.info(f"Restored example {example_id}")
        return True

    def get_example(self, example_id: int) -> Optional[QueryExample]:
        """Get a query example by ID.
        
        Args:
            example_id: Example ID
            
        Returns:
            Query example if found, None otherwise
        """
        return self._store._examples.get(example_id)

    def get_deleted_examples(
        self,
        max_age_days: Optional[float] = None
    ) -> Dict[int, Tuple[QueryExample, datetime]]:
        """Get deleted examples.
        
        Args:
            max_age_days: Optional maximum age in days
            
        Returns:
            Dictionary of deleted examples with deletion timestamps
        """
        if max_age_days is None:
            return self._deleted_examples.copy()
            
        now = datetime.now()
        return {
            k: (ex, ts) for k, (ex, ts) in self._deleted_examples.items()
            if (now - ts).total_seconds() / (24 * 3600) <= max_age_days
        }

    def cleanup_deleted_examples(self, max_age_days: float) -> int:
        """Remove old deleted examples.
        
        Args:
            max_age_days: Maximum age in days
            
        Returns:
            Number of examples removed
        """
        now = datetime.now()
        to_remove = [
            k for k, (_, ts) in self._deleted_examples.items()
            if (now - ts).total_seconds() / (24 * 3600) > max_age_days
        ]
        
        for k in to_remove:
            del self._deleted_examples[k]
            
        return len(to_remove)

    def _create_backup(self, reason: str) -> Optional[Path]:
        """Create a backup of the current state.
        
        Args:
            reason: Reason for backup
            
        Returns:
            Path to backup if created, None otherwise
        """
        if not self._backup_dir:
            return None
            
        self._backup_dir.mkdir(parents=True, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = self._backup_dir / f"backup_{timestamp}_{reason}.json"
        
        # Save current state
        state = {
            "examples": {
                str(k): v.model_dump() for k, v in self._store._examples.items()
            },
            "deleted_examples": {
                str(k): {
                    "example": ex.model_dump(),
                    "deleted_at": ts.isoformat()
                }
                for k, (ex, ts) in self._deleted_examples.items()
            },
            "metadata": {
                "reason": reason,
                "timestamp": timestamp
            }
        }
        
        with open(backup_path, "w") as f:
            json.dump(state, f, indent=2)
            
        # Cleanup old backups
        backups = sorted(self._backup_dir.glob("backup_*.json"))
        if len(backups) > self._max_backup_count:
            for old_backup in backups[:-self._max_backup_count]:
                old_backup.unlink()
                
        return backup_path
