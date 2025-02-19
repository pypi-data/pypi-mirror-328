"""Initialize test patches."""
from unittest.mock import Mock

# Create mock modules
mock_modules = {
    'experiment': Mock(),
    'stimulus': Mock(),
    'behavior': Mock(),
    'recording': Mock(),
    'mice': Mock(),
    'interface': Mock()
}

# Create mock connection
mock_conn = Mock()

# Mock create_virtual_modules function
def mock_create_virtual_modules(*args, **kwargs):
    """Mock virtual module creation."""
    return mock_modules, mock_conn