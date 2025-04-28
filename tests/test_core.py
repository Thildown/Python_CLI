import unittest
import os
import json
import tempfile
from unittest.mock import patch

# Import modules to test
from task_manager.core import add_task, list_tasks, delete_task, save_tasks, load_tasks

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        """Setup test environment."""
        # Create a temporary file for tasks
        self.test_file_fd, self.test_file_path = tempfile.mkstemp()
        self.patcher = patch('task_manager.core.TASKS_FILE', self.test_file_path)
        self.mock_tasks_file = self.patcher.start()
        
        # Initialize with empty tasks
        with open(self.test_file_path, 'w') as f:
            json.dump([], f)
    
    def tearDown(self):
        """Clean up after tests."""
        self.patcher.stop()
        os.close(self.test_file_fd)
        os.unlink(self.test_file_path)
    
    def test_add_task(self):
        """Test adding a task."""
        # Add a task
        task = add_task("Test task", "high")
        self.assertIsNotNone(task)
        self.assertEqual(task["description"], "Test task")
        self.assertEqual(task["priority"], "high")
        
        # Verify it was added
        tasks = load_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["description"], "Test task")
    
    def test_add_task_invalid_priority(self):
        """Test adding a task with invalid priority."""
        task = add_task("Invalid priority task", "super-high")
        self.assertIsNotNone(task)
        self.assertEqual(task["priority"], "medium")  # Should default to medium
    
    def test_delete_task(self):
        """Test deleting a task."""
        # Add a task
        task = add_task("Task to delete", "low")
        task_id = task["id"]
        
        # Verify it was added
        tasks = load_tasks()
        self.assertEqual(len(tasks), 1)
        
        # Delete the task
        result = delete_task(task_id)
        self.assertTrue(result)
        
        # Verify it was deleted
        tasks = load_tasks()
        self.assertEqual(len(tasks), 0)
    
    def test_delete_nonexistent_task(self):
        """Test deleting a non-existent task."""
        result = delete_task("non-existent-id")
        self.assertFalse(result)
    
    def test_list_tasks(self):
        """Test listing tasks."""
        # Add some tasks
        add_task("Task 1", "high")
        add_task("Task 2", "medium")
        
        # List tasks
        tasks = list_tasks()
        self.assertEqual(len(tasks), 2)

if __name__ == "__main__":
    unittest.main()