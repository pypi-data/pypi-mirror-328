from concurrent.futures import ThreadPoolExecutor
from unittest import mock
from unittest.mock import patch, PropertyMock
import unittest

from ciocore import api_client
from ciocore.downloader.base_downloader import (
    BaseDownloader,
    DEFAULT_DELAY,
    DEFAULT_JITTER,
    DEFAULT_MAX_ATTEMPTS,
    DEFAULT_NUM_THREADS,
    DEFAULT_PAGE_SIZE,
    DEFAULT_PROGRESS_INTERVAL,
    ensure_writable_output_path,
    ensure_path_valid
)

class TestBaseDownloaderInit(unittest.TestCase):
    def test_default_values(self):
        # Create an instance of the class
        downloader = BaseDownloader()

        # Assertions
        self.assertIsNone(downloader.output_path)
        self.assertFalse(downloader.force)
        self.assertEqual(downloader.num_threads, DEFAULT_NUM_THREADS)
        self.assertEqual(downloader.max_queue_size, DEFAULT_NUM_THREADS * 2)
        self.assertEqual(
            downloader.progress_interval, DEFAULT_PROGRESS_INTERVAL / 1000.0
        )
        self.assertEqual(downloader.page_size, DEFAULT_PAGE_SIZE)
        self.assertIsInstance(downloader.client, api_client.ApiClient)
        self.assertEqual(downloader.max_attempts, DEFAULT_MAX_ATTEMPTS)
        self.assertEqual(downloader.delay, DEFAULT_DELAY)
        self.assertEqual(downloader.jitter, DEFAULT_JITTER)
        self.assertIsNone(downloader.regex)

    def test_custom_values(self):
        output_path = "/path/to/destination"
        num_threads = 4
        progress_interval = 500
        page_size = 10
        force = True
        regex = r"\d+"
        max_attempts = 3
        delay = 2
        jitter = 0.5

        downloader = BaseDownloader(
            output_path=output_path,
            num_threads=num_threads,
            progress_interval=progress_interval,
            page_size=page_size,
            force=force,
            regex=regex,
            max_attempts=max_attempts,
            delay=delay,
            jitter=jitter,
        )

        # Assertions
        self.assertEqual(downloader.output_path, output_path)
        self.assertTrue(downloader.force)
        self.assertEqual(downloader.num_threads, num_threads)
        self.assertEqual(downloader.max_queue_size, num_threads * 2)
        self.assertAlmostEqual(downloader.progress_interval, progress_interval / 1000.0)
        self.assertEqual(downloader.page_size, page_size)
        self.assertIsInstance(downloader.client, api_client.ApiClient)
        self.assertEqual(downloader.max_attempts, max_attempts)
        self.assertEqual(downloader.delay, delay)
        self.assertEqual(downloader.jitter, jitter)
        self.assertIsNotNone(downloader.regex)


class TestBaseDownloaderRun(unittest.TestCase):
    def setUp(self):
        self.downloader = BaseDownloader()

    def tearDown(self):
        pass

    def test_run_method(self):
        with patch(
            "ciocore.downloader.base_downloader.ThreadPoolExecutor"
        ) as mock_executor:
            my_mock_executor = mock.MagicMock(spec=ThreadPoolExecutor)

            mock_executor.return_value.__enter__.return_value = my_mock_executor

            tasks = [{"id": 1, "name": "task1"}, {"id": 2, "name": "task2"}]
            next_locator = False
            mock_get_some_tasks = mock.MagicMock(return_value=(tasks, next_locator))

            self.downloader.get_some_tasks = mock_get_some_tasks
            self.downloader.download_tasks = mock.MagicMock()
            self.downloader.event_queue = mock.MagicMock()

            self.downloader.run()

            mock_get_some_tasks.assert_called_with(None)
            self.downloader.download_tasks.assert_called_with(tasks, my_mock_executor)


class TestEnsureWritableOutputPath(unittest.TestCase):

    @patch("ciocore.downloader.base_downloader.ensure_path_valid", return_value=True)
    def test_user_specified_path_is_returned_with_job_id_if_valid(
        self, mock_ensure_path_valid
    ):
        file_info = {"job_id": "00123", "task_id": "task1", "relative_path": "file.txt"}
        task_info = {"job_id": "00123"}
        user_specified_path = "/my/new/path"

        result = ensure_writable_output_path(file_info, task_info, user_specified_path)
        self.assertEqual(result, "/my/new/path/00123")
        mock_ensure_path_valid.assert_called_with("/my/new/path/00123")

    @patch("ciocore.downloader.base_downloader.ensure_path_valid")
    @patch("ciocore.downloader.base_downloader.get_fallback_path")
    def test_user_specified_path_is_invalid_so_fallback_path_is_returned(
        self, mock_get_fallback_path, mock_ensure_path_valid
    ):
        file_info = {"job_id": "00123", "task_id": "task1", "relative_path": "file.txt"}
        task_info = {"job_id": "00123"}
        user_specified_path = "/invalid/path"

        # Mock ensure_path_valid to return False for user_specified_path and True for fallback path
        mock_ensure_path_valid.side_effect = lambda path: "invalid" not in path

        # Mock get_fallback_path to return a specific fallback path
        fallback_path = "/valid/fallback/path/00123"
        mock_get_fallback_path.return_value = fallback_path

        result = ensure_writable_output_path(file_info, task_info, user_specified_path)

        # Assert that the fallback path is returned
        self.assertEqual(result, fallback_path)

        # Ensure that ensure_path_valid was called with the correct paths
        mock_ensure_path_valid.assert_any_call("/invalid/path/00123")
        mock_ensure_path_valid.assert_any_call(fallback_path)

        # Ensure get_fallback_path was called with the correct job_id
        mock_get_fallback_path.assert_called_with(task_info["job_id"])

    @patch("ciocore.downloader.base_downloader.ensure_path_valid")
    @patch("ciocore.downloader.base_downloader.get_fallback_path") 
    def test_user_specified_path_and_fallback_path_are_invalid_so_none_is_returned(
        self, mock_get_fallback_path, mock_ensure_path_valid
    ):
        file_info = {
            "job_id": "00123",
            "task_id": "task1",
            "relative_path": "file.txt"
        }
        task_info = {"job_id": "00123"}
        user_specified_path = "/invalid/user/path"

        # Mock ensure_path_valid to return False for all paths
        mock_ensure_path_valid.return_value = False

        # Mock get_fallback_path to return a specific fallback path
        mock_get_fallback_path.return_value = "/invalid/fallback/path/00123"

        result = ensure_writable_output_path(file_info, task_info, user_specified_path)

        # Assert that None is returned when no valid paths are found
        self.assertIsNone(result)

        # Ensure that ensure_path_valid was called with both paths
        mock_ensure_path_valid.assert_any_call("/invalid/user/path/00123")
        mock_ensure_path_valid.assert_any_call("/invalid/fallback/path/00123")

        # Ensure get_fallback_path was called with the correct job_id
        mock_get_fallback_path.assert_called_with(task_info["job_id"])

    @patch("ciocore.downloader.base_downloader.ensure_path_valid", return_value=True)
    def test_output_dir_is_returned_if_valid_and_no_user_specified_path(
        self, mock_ensure_path_valid
    ):
        file_info = {"output_dir": "/valid/output/dir", "job_id": "00123", "task_id": "task1", "relative_path": "file.txt"}
        task_info = {"job_id": "00123"}
 
        result = ensure_writable_output_path(file_info, task_info)

        # Assert that the output directory from file_info is returned
        self.assertEqual(result, file_info["output_dir"])

        # Ensure that ensure_path_valid was called with the correct path
        mock_ensure_path_valid.assert_called_with(file_info["output_dir"])

    @patch("ciocore.downloader.base_downloader.ensure_path_valid")
    @patch("ciocore.downloader.base_downloader.get_fallback_path")
    def test_fallback_path_is_returned_if_output_dir_is_invalid_and_no_user_specified_path(
        self, mock_get_fallback_path, mock_ensure_path_valid
    ):
        file_info = {"output_dir": "/invalid/output/dir", "job_id": "00123", "task_id": "task1", "relative_path": "file.txt"}
        task_info = {"job_id": "00123"}
        user_specified_path = None  # No user-specified path
        fallback_path = "/valid/fallback/path/00123"

        # Mock ensure_path_valid to return False for output_dir and True for fallback path
        mock_ensure_path_valid.side_effect = lambda path: path == fallback_path

        # Mock get_fallback_path to return a specific fallback path
        mock_get_fallback_path.return_value = fallback_path

        result = ensure_writable_output_path(file_info, task_info, user_specified_path)

        # Assert that the fallback path is returned
        self.assertEqual(result, fallback_path)

        # Ensure that ensure_path_valid was called with the correct paths
        mock_ensure_path_valid.assert_any_call(file_info["output_dir"])
        mock_ensure_path_valid.assert_any_call(fallback_path)

        # Ensure get_fallback_path was called with the correct job_id
        mock_get_fallback_path.assert_called_with(task_info["job_id"])

    @patch("ciocore.downloader.base_downloader.ensure_path_valid", return_value=False)
    @patch("ciocore.downloader.base_downloader.get_fallback_path")
    def test_none_is_returned_if_output_dir_and_fallback_path_are_invalid(
        self, mock_get_fallback_path, mock_ensure_path_valid
    ):
        file_info = {"output_dir": "/invalid/output/dir", "job_id": "00123", "task_id": "task1", "relative_path": "file.txt"}
        task_info = {"job_id": "00123"}
        user_specified_path = None  # No user-specified path
        fallback_path = "/invalid/fallback/path/00123"

        # Mock get_fallback_path to return a specific fallback path
        mock_get_fallback_path.return_value = fallback_path

        result = ensure_writable_output_path(file_info, task_info, user_specified_path)

        # Assert that None is returned when no valid paths are found
        self.assertIsNone(result)

        # Ensure that ensure_path_valid was called with both paths
        mock_ensure_path_valid.assert_any_call(file_info["output_dir"])
        mock_ensure_path_valid.assert_any_call(fallback_path)

        # Ensure get_fallback_path was called with the correct job_id
        mock_get_fallback_path.assert_called_with(task_info["job_id"])


class TestEnsurePathValid(unittest.TestCase):

    @patch("ciocore.downloader.base_downloader.os.makedirs")
    @patch("ciocore.downloader.base_downloader.os")
    def test_drive_letter_path_on_linux_returns_false(self, mock_os, mock_makedirs):
        # Set os.name to 'posix' to simulate a Linux environment
        mock_os.name = 'posix'

        # Define a path with a drive letter
        path_with_drive_letter = "C:/some/path"

        # Call ensure_path_valid and assert it returns False
        result = ensure_path_valid(path_with_drive_letter)
        self.assertFalse(result)

        # Ensure os.makedirs is not called since the path is already invalid
        mock_makedirs.assert_not_called()
        
        
    @patch("ciocore.downloader.base_downloader.os.makedirs")
    @patch("ciocore.downloader.base_downloader.os")
    def test_drive_letter_path_on_windows_calls_makedirs_and_returns_true(self, mock_os, mock_makedirs):
        # Set os.name to 'nt' to simulate a Windows environment
        mock_os.name = 'nt'

        # Define a path with a drive letter
        path_with_drive_letter = "C:/some/path"

        # Call ensure_path_valid and assert it returns True
        result = ensure_path_valid(path_with_drive_letter)
        self.assertTrue(result)

        # Ensure os.makedirs is called since the path is valid
        mock_makedirs.assert_called_with(path_with_drive_letter, exist_ok=True)
