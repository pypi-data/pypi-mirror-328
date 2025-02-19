"""Mock datajoint module for testing."""
from unittest.mock import Mock

# Create mock connection
mock_conn = Mock()
mock_conn.connect = Mock()

# Create mock Connection class
Connection = Mock()
Connection.return_value = mock_conn

# Create mock virtual module
def create_virtual_module(*args, **kwargs):
    """Mock virtual module creation."""
    return Mock()

# Create mock config
config = {
    "database.host": "127.0.0.1",
    "database.user": "root",
    "database.password": "test",
    "database.port": 3306,
    "connection.init_function": None,
    "connection.charset": "",
    "loglevel": "INFO",
    "safemode": True,
    "fetch_format": "array",
    "display.limit": 12,
    "display.width": 14,
    "display.show_tuple_count": True,
    "database.reconnect": True,
    "enable_python_native_blobs": True,
}

# Export the mocks
__all__ = ['Connection', 'create_virtual_module', 'mock_conn', 'config']