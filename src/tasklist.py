import json
from tabulate import tabulate
from enum import Enum
from .task import Task

class TaskList:
    def __init__(self, file_path):
        self.file_path = file_path
        self.tasks = self.get_tasks()
    
    def get_tasks(self):
        with open(self.file_path, 'r') as file:
            file_data = json.load(file)
        return [Task(task['desc'], task.get('is_complete')) for task in file_data['tasks']]

    def display_tasks(self):
        table = [[i + 1, task.desc, "Yes" if task.is_complete else "No"] for i, task in enumerate(self.tasks)]
        print(tabulate(table, headers=["ID", "Description", "Completed"], tablefmt="fancy_grid"))

    def add_task(self, desc):
        print(f"New task added: {desc}")
        last_task_num = len(self.tasks)
        new_task = {
            "id": last_task_num + 1,
            "desc": desc,
            "is_complete": 0 
        }
        with open(self.file_path, 'r+') as file:
            file_data = json.load(file)
            print(f"File_data: {file_data}")
            file_data["tasks"].append(new_task)
            file.seek(0)
            json.dump(file_data, file, indent=4)
        self.tasks.append(Task(desc))
        self.display_tasks()

            


    def complete_task(self):
        pass

class Action(Enum):
    ADD = 'add'
    UPDATE = 'update'
    COMPLETE = 'complete'
    DELETE = 'delete'
    EXIT = 'x'
