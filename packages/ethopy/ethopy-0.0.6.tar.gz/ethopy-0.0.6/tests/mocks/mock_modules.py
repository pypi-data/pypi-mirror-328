"""Mock modules for testing."""
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

# Mock scipy.stats
mock_stats = Mock()
mock_stats.norm = Mock()
mock_stats.norm.cdf = Mock(return_value=0.5)
mock_stats.norm.ppf = Mock(return_value=0.0)

# Mock sklearn.metrics
mock_metrics = Mock()
mock_metrics.roc_auc_score = Mock(return_value=0.75)

# Mock create_virtual_modules function
def mock_create_virtual_modules(*args, **kwargs):
    """Mock virtual module creation."""
    return mock_modules, mock_conn