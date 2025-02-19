import logging
import platform
import socket
import threading
from datetime import datetime
from queue import PriorityQueue
from unittest.mock import Mock, patch

import pytest
from freezegun import freeze_time

# Import after mocking in conftest.py
from ethopy.core.logger import Logger, PrioritizedItem
from ethopy.utils.task import Task


@pytest.fixture
def mock_virtual_modules():
    """Create mock virtual modules for database schemas."""
    mock_modules = {
        "experiment": Mock(),
        "stimulus": Mock(),
        "behavior": Mock(),
        "recording": Mock(),
        "mice": Mock(),
        "interface": Mock()
    }
    return mock_modules


@pytest.fixture
def mock_create_virtual_modules(mock_virtual_modules):
    """Mock the create_virtual_modules function."""
    with patch("ethopy.core.logger.create_virtual_modules") as mock_create:
        mock_create.return_value = (mock_virtual_modules, Mock())
        yield mock_create


@pytest.fixture
def mock_local_conf():
    """Mock the local_conf configuration."""
    with patch("ethopy.core.logger.local_conf") as mock_conf:
        mock_conf.get.side_effect = lambda key: {
            "source_path": "/test/source",
            "target_path": "/test/target"
        }.get(key)
        yield mock_conf


@pytest.fixture
def logger(mock_create_virtual_modules, mock_local_conf):
    """Create a Logger instance with mocked dependencies."""
    with patch("threading.Thread"):
        logger = Logger(task=False)
        logger.thread_end = threading.Event()
        logger.thread_lock = threading.Lock()
        logger.queue = PriorityQueue()
        return logger


def test_prioritized_item_creation():
    """Test PrioritizedItem creation and default values."""
    item = PrioritizedItem(table="test_table", tuple={"id": 1})
    
    assert item.table == "test_table"
    assert item.tuple == {"id": 1}
    assert item.schema == "experiment"  # default value
    assert not item.replace  # default value
    assert not item.block  # default value
    assert item.priority == 50  # default value
    assert not item.error  # default value
    assert item.ignore_extra_fields  # default value


def test_prioritized_item_comparison():
    """Test PrioritizedItem priority comparison."""
    item1 = PrioritizedItem(table="test", tuple={}, priority=1)
    item2 = PrioritizedItem(table="test", tuple={}, priority=2)
    
    assert item1 < item2  # Lower priority number means higher priority


def test_logger_initialization(logger):
    """Test Logger initialization."""
    assert logger.setup == socket.gethostname()
    assert isinstance(logger.task, Task)
    assert logger.manual_run is False
    assert logger.setup_status == "ready"
    assert isinstance(logger.queue, PriorityQueue)
    assert logger.total_reward == 0
    assert logger.curr_state == ""
    assert logger.source_path == "/test/source"
    assert logger.target_path == "/test/target"


# @patch("platform.uname")
# def test_check_if_raspberry_pi(mock_uname, logger):
#     """Test Raspberry Pi detection."""
#     # Test Linux ARM system (Raspberry Pi)
#     mock_uname.return_value = Mock(system="Linux", machine="aarch64")
#     assert logger._check_if_raspberry_pi() is True
    
#     # Test Linux non-ARM system
#     mock_uname.return_value = Mock(system="Linux", machine="x86_64")
#     assert logger._check_if_raspberry_pi() is False
    
#     # Test non-Linux system
#     mock_uname.return_value = Mock(system="Darwin", machine="arm64")
#     assert logger._check_if_raspberry_pi() is False


# def test_put_method(logger):
#     """Test the put method for queueing items."""
#     # Test non-blocking put
#     logger.put(table="test", tuple={"id": 1}, block=False)
#     assert logger.queue.qsize() == 1
    
#     # Test blocking put
#     logger.put(table="test", tuple={"id": 2}, block=True)
#     assert logger.queue.qsize() == 2
    
#     # Verify items were queued with correct priorities
#     item1 = logger.queue.get()
#     assert item1.tuple == {"id": 1}
#     assert item1.priority == 50
    
#     item2 = logger.queue.get()
#     assert item2.tuple == {"id": 2}
#     assert item2.priority == 50


# def test_insert_item(logger):
#     """Test the _insert_item method."""
#     mock_table = Mock()
#     item = PrioritizedItem(table="test", tuple={"id": 1}, replace=True)
    
#     logger._insert_item(item, mock_table)
    
#     mock_table.insert1.assert_called_once_with(
#         {"id": 1},
#         ignore_extra_fields=True,
#         skip_duplicates=False,
#         replace=True
#     )


# def test_validate_item(logger):
#     """Test the _validate_item method."""
#     mock_table = Mock()
#     mock_table.primary_key = ["id"]
#     item = PrioritizedItem(
#         table="test",
#         tuple={"id": 1, "value": "test"},
#         validate=True
#     )
    
#     # Test when item exists
#     mock_table.__and__ = Mock(return_value=Mock(__len__=Mock(return_value=1)))
#     logger._validate_item(item, mock_table)  # Should not raise
    
#     # Test when item doesn't exist initially but appears later
#     mock_table.__and__ = Mock(return_value=Mock(__len__=Mock(side_effect=[0, 1])))
#     with patch("time.sleep") as mock_sleep:
#         logger._validate_item(item, mock_table)
#         mock_sleep.assert_called_once_with(0.5)


# def test_handle_insert_error(logger, caplog):
#     """Test error handling during insertion."""
#     item = PrioritizedItem(table="test", tuple={"id": 1}, priority=1)
#     mock_table = Mock()
#     exception = Exception("Test error")
    
#     with caplog.at_level(logging.WARNING):
#         logger._handle_insert_error(item, mock_table, exception, logger.queue)
    
#     assert "Failed to insert" in caplog.text
#     assert item.error is True
#     assert item.priority == 3  # Original priority + 2
#     assert logger.queue.qsize() == 1


# @freeze_time("2024-01-01 12:00:00")
# def test_log_method(logger):
#     """Test the log method."""
#     logger.trial_key = {"animal_id": 1, "session": 1, "trial_idx": 1}
#     logger.logger_timer.start()
    
#     # Test basic logging
#     timestamp = logger.log("Trial", {"state": "test_state"})
    
#     assert timestamp == logger.logger_timer.elapsed_time()
#     assert logger.queue.qsize() == 1
    
#     # Verify queued item
#     item = logger.queue.get()
#     assert item.table == "Trial"
#     assert item.tuple["animal_id"] == 1
#     assert item.tuple["session"] == 1
#     assert item.tuple["trial_idx"] == 1
#     assert item.tuple["state"] == "test_state"
#     assert item.tuple["time"] == timestamp


# def test_acquire_lock(logger):
#     """Test the acquire_lock context manager."""
#     mock_lock = Mock()
#     mock_lock.acquire = Mock()
#     mock_lock.release = Mock()
    
#     # Test normal operation
#     with logger.acquire_lock(mock_lock):
#         mock_lock.acquire.assert_called_once()
#         assert not mock_lock.release.called
#     mock_lock.release.assert_called_once()
    
#     # Test with exception
#     mock_lock.reset_mock()
#     with pytest.raises(ValueError):
#         with logger.acquire_lock(mock_lock):
#             raise ValueError("Test error")
#     mock_lock.acquire.assert_called_once()
#     mock_lock.release.assert_called_once()


# def test_setup_schema(logger):
#     """Test setting up additional schema."""
#     mock_schema = {"test_schema": "test_value"}
#     mock_virtual_module = Mock()
    
#     with patch("datajoint.create_virtual_module",
#               return_value=mock_virtual_module) as mock_create:
#         logger.setup_schema(mock_schema)
        
#         # Verify schema was created with correct parameters
#         assert mock_create.call_count == 2  # Called for both global and private
#         assert "test_schema" in logger._schemata
#         assert logger._schemata["test_schema"] == mock_virtual_module


# @freeze_time("2024-01-01 12:00:00")
# def test_update_setup_info(logger):
#     """Test updating setup information."""
#     logger.setup_info = {"setup": "test_setup", "status": "running"}
#     logger.trial_key = {"trial_idx": 5}
#     logger.total_reward = 10.5
#     logger.curr_state = "test_state"
#     logger.ping_timer.start()
    
#     # Simulate elapsed time
#     with freeze_time("2024-01-01 12:01:00"):
#         logger._update_setup_info(update_period=1000)
    
#     assert logger.queue.qsize() == 1
#     item = logger.queue.get()
#     assert item.table == "Control"
#     assert item.tuple["setup"] == "test_setup"
#     assert item.tuple["status"] == "running"
#     assert item.tuple["trials"] == 5
#     assert item.tuple["total_liquid"] == 10.5
#     assert item.tuple["state"] == "test_state"
#     assert item.tuple["last_ping"] == "2024-01-01 12:01:00"
#     assert item.priority == 1
#     assert item.replace is True