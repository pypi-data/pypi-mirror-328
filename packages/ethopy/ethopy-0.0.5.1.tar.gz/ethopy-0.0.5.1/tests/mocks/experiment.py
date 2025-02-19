"""Mock version of the experiment module for testing."""
from unittest.mock import Mock

# Mock scipy.stats
stats = Mock()
stats.norm = Mock()
stats.norm.cdf = Mock(return_value=0.5)
stats.norm.ppf = Mock(return_value=0.0)

# Mock sklearn.metrics
metrics = Mock()
metrics.roc_auc_score = Mock(return_value=0.75)

# Export the mocks
__all__ = ['stats', 'metrics']