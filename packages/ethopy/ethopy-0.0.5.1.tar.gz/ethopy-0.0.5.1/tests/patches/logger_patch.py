"""Patch for logger module to allow testing without database connection."""
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

# Replace the _set_connection function
def mock_set_connection():
    """Mock database connection setup."""
    global experiment, stimulus, behavior, interface, recording, mice, public_conn
    experiment = mock_modules['experiment']
    stimulus = mock_modules['stimulus']
    behavior = mock_modules['behavior']
    recording = mock_modules['recording']
    mice = mock_modules['mice']
    interface = mock_modules['interface']
    public_conn = mock_conn

# Export the mock objects
__all__ = ['mock_modules', 'mock_conn', 'mock_set_connection']