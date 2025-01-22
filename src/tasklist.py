import json
from task import Task

class TaskList:
    def __init__(self, file_path):
        self.file_path = file_path
        self.tasks = self.load_tasks()
    
    def load_tasks(self):
        with open(self.file_path, 'r') as file:
            data = json.load(file)
        return [Task(task['desc'], task.get('is_complete')) for task in data['tasks']]

    
    def display_tasks(self):
        data = self.tasks
        for i in range(len(data)):
            print(f"{i + 1}. {data[i].desc}")

    def add_task(self, desc):
        pass

    def complete_stask(self):
        pass
