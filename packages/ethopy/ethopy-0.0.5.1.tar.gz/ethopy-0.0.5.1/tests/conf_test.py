import sys
from pathlib import Path
import pytest
from unittest.mock import Mock, patch

# Add tests directory to Python path
tests_dir = Path(__file__).parent
sys.path.insert(0, str(tests_dir))

# Import mocks
from mocks.mock_modules import mock_stats, mock_metrics
from mocks.datajoint_mock import Connection, create_virtual_module

# Create mock modules
mock_modules = {
    'scipy': Mock(stats=mock_stats),
    'sklearn': Mock(metrics=mock_metrics),
    'datajoint': Mock(
        Connection=Connection,
        create_virtual_module=create_virtual_module
    ),
}

# Apply patches before any imports
for module_name, mock_module in mock_modules.items():
    sys.modules[module_name] = mock_module
    if module_name == 'scipy':
        sys.modules['scipy.stats'] = mock_stats
    elif module_name == 'sklearn':
        sys.modules['sklearn.metrics'] = mock_metrics

@pytest.fixture(autouse=True)
def mock_database_connection():
    """Mock database connection for all tests."""
    mock_modules = {
        'experiment': Mock(),
        'stimulus': Mock(),
        'behavior': Mock(),
        'recording': Mock(),
        'mice': Mock(),
        'interface': Mock()
    }
    with patch('ethopy.utils.helper_functions.create_virtual_modules',
               return_value=(mock_modules, Mock())):
        yield mock_modules

@pytest.fixture(autouse=True)
def mock_scipy_stats():
    """Mock scipy.stats for all tests."""
    with patch('scipy.stats', mock_stats):
        yield mock_stats