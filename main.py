import click as ck
import json
from commands import filter_commands, modification_commands, removal_commands
import Constants as consts


#TODO: Leer los errores que se pueden generar usando el modulo JSON e intentar generar los errores apropósito durante el testing para ver si se generan, y manejarlos (try...except) si ocurren.
#TODO: Integrar el modulo Click para la interfaz de uso (Integrar la clase datetime de el modulo datetime para la due_date).

@ck.group
def daily_tasks():
    pass


@daily_tasks.command
def create_tasks_file():
    """Create the tasks file (it will be empty)."""
    with open('Tasks.json', 'w', encoding='utf-8') as tasks_file:
        json.dump([], tasks_file)


@daily_tasks.command
@ck.option('-d', '--description', required=True, type=ck.STRING, help="Describe your task.")
@ck.option('-p', '--priority', type=ck.Choice(consts.PRIORITIES, case_sensitive=False), help="Choose a priority to your task.")
@ck.option('-dd', '--due-date', type=ck.DateTime(formats=consts.DUE_DATE_FORMAT), help="Set a due date to your task.")
@ck.option('-s', '--status', type=ck.Choice(consts.STATUS, case_sensitive=False), help="Choose a status to your task.")
def add_task(description, priority, due_date, status):
    """Create a new task"""
    with open('Tasks.json', 'r', encoding='utf-8') as tasks_file_read:
        tasks = json.load(tasks_file_read)

    amount_of_tasks = len(tasks)
    task_id = amount_of_tasks + 1
    priority_upper = priority.upper()
    status_capitalize = status.capitalize()
    tasks.append(
        {
            "id": task_id,
            "description": f"{description}",
            "priority": f"{priority_upper}",
            "due_date": f"{due_date}",
            "status": f"{status_capitalize}"
        }
    )
    
    with open('Tasks.json', 'w', encoding='utf-8') as tasks_file_write:
        json.dump(tasks, tasks_file_write, indent=2)


@daily_tasks.command
def view_tasks():
    """Shows you all your tasks"""
    with open('Tasks.json', 'r', encoding='utf-8') as tasks_file:
        tasks = json.load(tasks_file)

    for task in tasks:
        print(task)


### TESTS ###
#initialize_tasks_file()
#add_task("First task", "m", "28/2/2024")
#view_tasks()
#modify_description(1, "Change task")
#modification_commands.modify_priority(1, "H")
#modify_due_date(1, "2024-2-29")
#modification_commands.modify_status(1, "In progress")
#delete_done_tasks()
#delete_task(1)
#filter_commands.filter_tasks_by_priority("H")
#filter_tasks_by_due_date("2024/2/29")
#filter_commands.filter_tasks_by_status("Done")

if __name__ == '__main__':
    daily_tasks()