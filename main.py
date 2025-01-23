#!/usr/bin/env python3
# filepath: /Users/mcriqui/workspace/github.com/mcriq/cli_todo/main.py

from src.tasklist import TaskList, Action

def main():
    is_running = True
    task_list = TaskList('./data/dummy_data.json')
    print("Your active tasks:")
    task_list.display_tasks()
    while is_running:
        user_action = input('What action would you like to take?\n(Try add, comp, del, or x to exit): ')
        if user_action.lower() not in Action._value2member_map_:
            invalid_command()
            
        if user_action.lower() == Action.EXIT.value:
            exit_program()
            is_running = False

        if user_action == Action.ADD.value:
            description = input("Enter your todo: ")
            task_list.add_task(description)
            
        if user_action == Action.COMPLETE.value:
            task_list.complete_task()
            
        if user_action == Action.DELETE.value:
            task_list.delete_task()
            


def invalid_command():
    print('\n================Invalid command================\n')

def exit_program():
    print('Exiting todo list. Goodbye...')

if __name__ == "__main__":
    main()