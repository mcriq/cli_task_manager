import unittest
import json
import os
from src.tasklist import TaskList, Task

class TestTaskList(unittest.TestCase):
    def setUp(self):
        # Create a temporary JSON file for testing
        self.test_file_path = './data/test_dummy_data.json'
        with open(self.test_file_path, 'w') as file:
            json.dump({"tasks": []}, file)
        self.task_list = TaskList(self.test_file_path)

    def tearDown(self):
        # Remove the temporary JSON file after testing
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)

    def test_add_task(self):
        self.task_list.add_task("Test Task")
        self.assertEqual(len(self.task_list.tasks), 1)
        self.assertEqual(self.task_list.tasks[0].desc, "Test Task")
        self.assertFalse(self.task_list.tasks[0].is_complete)

    def test_complete_task(self):
        self.task_list.add_task("Test Task")
        self.task_list.complete_task()
        self.assertTrue(self.task_list.tasks[0].is_complete)

    def test_delete_task(self):
        self.task_list.add_task("Test Task")
        self.task_list.delete_task()
        self.assertEqual(len(self.task_list.tasks), 0)

if __name__ == '__main__':
    unittest.main()