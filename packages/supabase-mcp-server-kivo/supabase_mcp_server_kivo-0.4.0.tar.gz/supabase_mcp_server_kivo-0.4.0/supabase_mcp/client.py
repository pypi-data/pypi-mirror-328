from dataclasses import dataclass
from typing import Any

import psycopg
from psycopg.errors import InsufficientPrivilege, UndefinedColumn, UndefinedTable
from psycopg_pool import ConnectionPool
from tenacity import retry, stop_after_attempt, wait_exponential

from supabase_mcp.exceptions import ConnectionError, PermissionError, QueryError
from supabase_mcp.logger import logger
from supabase_mcp.settings import Settings, settings


@dataclass
class QueryResult:
    """Represents a query result with metadata."""

    rows: list[dict[str, Any]]
    count: int
    status: str


class SupabaseClient:
    """Connects to Supabase PostgreSQL database directly."""

    _instance = None  # Singleton instance

    def __init__(
        self,
        project_ref: str | None = None,
        db_password: str | None = None,
        settings_instance: Settings | None = None,
    ):
        """Initialize the PostgreSQL connection pool.

        Args:
            project_ref: Optional Supabase project reference. If not provided, will be taken from settings.
            db_password: Optional database password. If not provided, will be taken from settings.
            settings_instance: Optional Settings instance. If not provided, will use global settings.
        """
        self._pool = None
        self._settings = settings_instance or settings
        self.project_ref = project_ref or self._settings.supabase_project_ref
        self.db_password = db_password or self._settings.supabase_db_password
        self.db_url = self._get_db_url_from_supabase()

    def _get_db_url_from_supabase(self) -> str:
        """Create PostgreSQL connection string from settings."""
        if self.project_ref.startswith("127.0.0.1"):
            # Local development
            return f"postgresql://postgres:{self.db_password}@{self.project_ref}/postgres"

        # Production Supabase
        return (
            f"postgresql://postgres.{self.project_ref}:{self.db_password}"
            f"@aws-0-us-east-1.pooler.supabase.com:6543/postgres"
        )

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=4, max=15),
    )
    def _get_pool(self):
        """Get or create PostgreSQL connection pool with better error handling."""
        if self._pool is None:
            try:
                logger.debug(f"Creating connection pool for: {self.db_url.split('@')[1]}")
                self._pool = ConnectionPool(
                    conninfo=self.db_url,
                    min_size=1,
                    max_size=10,
                    kwargs={"autocommit": True},
                )
                logger.info("✓ Created PostgreSQL connection pool")
            except psycopg.OperationalError as e:
                logger.error(f"Failed to connect to database: {e}")
                raise ConnectionError(f"Could not connect to database: {e}") from e
            except Exception as e:
                logger.exception("Unexpected error creating connection pool")
                raise ConnectionError(f"Unexpected connection error: {e}") from e
        return self._pool

    @classmethod
    def create(
        cls,
        project_ref: str | None = None,
        db_password: str | None = None,
        settings_instance: Settings | None = None,
    ) -> "SupabaseClient":
        """Create and return a configured SupabaseClient instance.

        Args:
            project_ref: Optional Supabase project reference
            db_password: Optional database password
            settings_instance: Optional Settings instance
        """
        if cls._instance is None:
            cls._instance = cls(
                project_ref=project_ref,
                db_password=db_password,
                settings_instance=settings_instance,
            )
        return cls._instance

    def close(self):
        """Explicitly close the connection pool."""
        if self._pool is not None:
            try:
                self._pool.close()
                self._pool = None
                logger.info("Closed PostgreSQL connection pool")
            except Exception as e:
                logger.error(f"Error closing connection pool: {e}")

    def readonly_query(self, query: str, params: tuple = None) -> QueryResult:
        """Execute a SQL query and return structured results.

        Args:
            query: SQL query to execute
            params: Optional query parameters to prevent SQL injection

        Returns:
            QueryResult containing rows and metadata

        Raises:
            ConnectionError: When database connection fails
            QueryError: When query execution fails (schema or general errors)
            PermissionError: When user lacks required privileges
        """
        if self._pool is None:
            # Reinitialize pool if it was closed
            self._pool = self._get_pool()

        pool = self._get_pool()
        with pool.connection() as conn:
            with conn.cursor() as cur:
                try:
                    cur.execute(query, params)
                    rows = cur.fetchall() or []
                    status = cur.statusmessage
                    return QueryResult(rows=rows, count=len(rows), status=status)
                except InsufficientPrivilege as e:
                    logger.error(f"Permission denied: {e}")
                    raise PermissionError(f"Access denied: {str(e)}") from e
                except (UndefinedTable, UndefinedColumn) as e:
                    logger.error(f"Schema error: {e}")
                    raise QueryError(str(e)) from e
                except psycopg.Error as e:
                    logger.error(f"Database error: {e.pgerror}")
                    raise QueryError(f"Query failed: {str(e)}") from e
