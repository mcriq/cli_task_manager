#!/Users/mcriqui/workspace/github.com/mcriq/cli_todo/venv/bin/python
from src.tasklist import TaskList

def main():
    is_running = True
    task_list = TaskList('./data/dummy_data.json')
    while is_running:
        print("Your active tasks:")
        task_list.display_tasks()
        user_action = input('What action would you like to take? ')
        print(user_action)
        is_running = False

if __name__ == "__main__":
    main()