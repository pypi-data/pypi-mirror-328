"""Mock version of the logger module for testing."""
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

# Mock the global variables
experiment = mock_modules['experiment']
stimulus = mock_modules['stimulus']
behavior = mock_modules['behavior']
recording = mock_modules['recording']
mice = mock_modules['mice']
interface = mock_modules['interface']
public_conn = mock_conn

# Mock the _set_connection function
def _set_connection():
    """Mock database connection setup."""
    pass  # Already set up above