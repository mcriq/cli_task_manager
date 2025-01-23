#!/usr/bin/env python3
# filepath: /Users/mcriqui/workspace/github.com/mcriq/cli_todo/main.py

from src.tasklist import TaskList, Action

def main():
    is_running = True
    task_list = TaskList('./data/dummy_data.json')
    print("Your active tasks:")
    task_list.display_tasks()
    while is_running:
        user_action = input('What action would you like to take?\n(Try add, update, complete, or delete)\n')
        if user_action.lower() not in Action:
            print('\n================Invalid command================\n')
            continue
        print(user_action)
        is_running = False

if __name__ == "__main__":
    main()