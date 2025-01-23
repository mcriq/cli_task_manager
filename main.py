#!/usr/bin/env python3
# filepath: /Users/mcriqui/workspace/github.com/mcriq/cli_todo/main.py

from src.tasklist import TaskList, Action

def main():
    is_running = True
    task_list = TaskList('./data/dummy_data.json')
    print("Your active tasks:")
    task_list.display_tasks()
    while is_running:
        user_action = input('What action would you like to take?\n(Try add, update, complete, delete, or x to exit): ')
        if user_action.lower() not in Action._value2member_map_:
            print('\n================Invalid command================\n')
            continue
        if user_action.lower() == Action.EXIT.value:
            print('Exiting todo list. Goodbye...')
            is_running = False
        if user_action == Action.ADD.value:
            description = input("Enter your todo: ")
            task_list.add_task(description)
            continue


if __name__ == "__main__":
    main()