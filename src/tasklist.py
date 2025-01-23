import json
from tabulate import tabulate
from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator
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
            file_data["tasks"].append(new_task)
            file.seek(0)
            json.dump(file_data, file, indent=4)
            file.truncate()
        self.tasks.append(Task(desc))
        self.display_tasks()


    def complete_task(self):
        choices = []
        for task in self.tasks:
            if task.is_complete == 0:
                choices.append(task.desc)
        choices.append(Choice(value=None, name="Exit"))

        action = inquirer.select(
        message="Select the task to complete:",
        choices=choices,
        default=None,
        ).execute()
        if action == None:
            self.display_tasks()
            return
        else:
            print(f"ACTION: {action}")
            with open(self.file_path, 'r+') as file:
                file_data = json.load(file)
                for item in file_data['tasks']:
                    if item["desc"] == action:
                        item["is_complete"] = 1
                file.seek(0)
                json.dump(file_data, file, indent=4)
                file.truncate()
            self.tasks = self.get_tasks()
            self.display_tasks()

    def delete_task(self):
        choices = []
        for task in self.tasks:
            choices.append(task.desc)
        choices.append(Choice(value=None, name="Exit"))

        action = inquirer.select(
        message="Select the task to delete:",
        choices=choices,
        default=None,
        ).execute()
        if action == None:
            self.display_tasks()
            return
        else:
            print(f"ACTION: {action}")
            with open(self.file_path, 'r+') as file:
                file_data = json.load(file)
                for item in file_data['tasks']:
                    if item["desc"] == action:
                        file_data['tasks'].remove(item)
                file.seek(0)
                json.dump(file_data, file, indent=4)
                file.truncate()
            self.tasks = self.get_tasks()
            self.display_tasks()



class Action(Enum):
    ADD = 'add'
    COMPLETE = 'comp'
    DELETE = 'del'
    EXIT = 'x'
