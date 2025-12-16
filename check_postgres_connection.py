import psycopg2
import sys
from contextlib import contextmanager
from psycopg2.extras import RealDictCursor
from typing import Dict, Any, Optional, Generator
from shared.core.config import settings


class PostgreSQLConnection:
    """PostgreSQL database connection handler with context manager support."""

    def __init__(self):
        self._connection = None
        self._cursor = None
        self._sslmode = "require" if settings.db_ssl else "disable"

    @property
    def connection_params(self) -> Dict[str, Any]:
        """Get database connection parameters."""
        return {
            "host": settings.db_host,
            "port": settings.db_port,
            "database": settings.db_name,
            "user": settings.db_user,
            "password": settings.db_password,
            "sslmode": self._sslmode,
            "cursor_factory": RealDictCursor,
            "connect_timeout": 10,
        }

    def connect(self) -> bool:
        """Establish connection to PostgreSQL database."""
        print("Connecting to PostgreSQL")
        self._print_connection_details()

        try:
            self._connection = psycopg2.connect(**self.connection_params)
            self._cursor = self._connection.cursor()
            return True
        except psycopg2.OperationalError as e:
            print(f"Connection failed: {e}")
            return False
        except psycopg2.Error as e:
            print(f"Database error: {e}")
            return False

    @contextmanager
    def get_cursor(self) -> Generator:
        """Context manager for database cursor operations."""
        if not self._connection or self._connection.closed:
            raise ConnectionError("Database not connected")

        try:
            yield self._cursor
            self._connection.commit()
        except Exception as e:
            self._connection.rollback()
            raise e

    def execute_query(self, query: str, params: tuple = None) -> Optional[Dict]:
        """Execute a query and return single result."""
        try:
            with self.get_cursor() as cursor:
                cursor.execute(query, params or ())
                return cursor.fetchone()
        except psycopg2.Error as e:
            print(f"Query execution failed: {e}")
            return None

    def test_connection(self) -> bool:
        """Test database connection with basic query."""
        result = self.execute_query("SELECT 1;")
        return result is not None and result.get('?column?') == 1

    def get_server_info(self) -> Optional[Dict[str, Any]]:
        """Retrieve PostgreSQL server version information."""
        result = self.execute_query("SELECT version();")
        return {"version": result["version"]} if result else None

    def get_session_info(self) -> Optional[Dict[str, Any]]:
        """Retrieve current session information."""
        return self.execute_query("""
            SELECT 
                current_database() AS database,
                current_user AS username,
                inet_client_addr() AS client_address,
                current_schema() AS current_schema
        """)

    def close(self):
        """Close database connection and cursor."""
        if self._cursor:
            self._cursor.close()
        if self._connection and not self._connection.closed:
            self._connection.close()

    def __enter__(self):
        """Context manager entry."""
        if not self.connect():
            raise ConnectionError("Failed to connect to database")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()

    def _print_connection_details(self):
        """Print connection details with masked password."""
        details = [
            f"Host: {settings.db_host}",
            f"Port: {settings.db_port}",
            f"Database: {settings.db_name}",
            f"User: {settings.db_user}",
            f"SSL: {'Enabled' if settings.db_ssl else 'Disabled'}",
            f"Password: {'*' * 8 if settings.db_password else 'Not set'}"
        ]
        print("\n".join(details))


def perform_database_check() -> bool:
    """
    Perform comprehensive database connection check.
    Returns True if all checks pass, False otherwise.
    """
    try:
        with PostgreSQLConnection() as db:
            print("Connection established successfully")

            # Test connection
            if not db.test_connection():
                print("Basic connection test failed")
                return False
            print("Basic connection test passed")

            # Get server info
            server_info = db.get_server_info()
            if server_info:
                print(f"Server Version: {server_info['version']}")
            else:
                print("Failed to retrieve server version")
                return False

            # Get session info
            session_info = db.get_session_info()
            if session_info:
                print("Session Information:")
                for key, value in session_info.items():
                    print(f"  {key}: {value}")
            else:
                print("Failed to retrieve session information")
                return False

            return True

    except ConnectionError as e:
        print(f"Connection error: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False


def main():
    """Main execution function."""
    separator = "=" * 50

    print(separator)
    print("PostgreSQL Database Connection Test")
    print(separator)

    success = perform_database_check()

    print(f"\n{separator}")
    if success:
        print("SUCCESS: All checks passed")
    else:
        print("FAILED: Database connection test")
        sys.exit(1)


if __name__ == "__main__":
    main()