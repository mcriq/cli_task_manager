import json
from tabulate import tabulate
from enum import Enum
from .task import Task

class TaskList:
    def __init__(self, file_path):
        self.file_path = file_path
        self.tasks = self.load_tasks()
    
    def load_tasks(self):
        with open(self.file_path, 'r') as file:
            data = json.load(file)
        return [Task(task['desc'], task.get('is_complete')) for task in data['tasks']]

    def display_tasks(self):
        table = [[i + 1, task.desc, "Yes" if task.is_complete else "No"] for i, task in enumerate(self.tasks)]
        print(tabulate(table, headers=["ID", "Description", "Completed"], tablefmt="fancy_grid"))

    def add_task(self, desc):
        pass

    def complete_stask(self):
        pass

class Action(Enum):
    ADD = 'add'
    UPDATE = 'update'
    COMPLETE = 'complete'
    DELETE = 'delete'
