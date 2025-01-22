#!/opt/homebrew/bin/python3
from tasklist import TaskList

def main():
    task_list = TaskList('./data/dummy_data.json')
    task_list.display_tasks()

main()