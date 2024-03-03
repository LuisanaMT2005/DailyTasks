import click as ck
from datetime import datetime
import json
from commands import filter_commands, modification_commands, removal_commands
import Constants as consts


#TODO: Leer los errores que se pueden generar usando el modulo JSON e intentar generar los errores apropósito durante el testing para ver si se generan, y manejarlos (try...except) si ocurren.
#TODO: Integrar el modulo Click para la interfaz de uso (Integrar la clase datetime de el modulo datetime para la due_date).

def get_due_date_default_value():
    """Get default value for due_date parameter"""
    today_datetime_obj = datetime.today()
    today_date_obj = today_datetime_obj.date()
    today_date_obj_formated = today_date_obj.strftime(consts.DUE_DATE_FORMAT[0])
    today_date_str_formated = str(today_date_obj_formated)

    return today_date_str_formated

# MAIN COMMANDS
@ck.group
def daily_tasks():
    pass


@daily_tasks.command
def create_tasks_file():
    """Create the tasks file (it will be empty)."""
    with open('Tasks.json', 'w', encoding='utf-8') as tasks_file:
        json.dump([], tasks_file)


@daily_tasks.command
@ck.option('-d', '--description',
           required=True, 
           type=ck.STRING, 
           help="Describe your task."
           )
@ck.option('-p', '--priority',
           type=ck.Choice(consts.PRIORITIES, case_sensitive=False),
           help="Choose a priority to your task.",
           default=consts.PRIORITIES[3]
           )
@ck.option('-dd', '--due-date',
           type=ck.DateTime(formats=consts.DUE_DATE_FORMAT),
           help="Set a due date to your task.",
           default=get_due_date_default_value()
           )
@ck.option('-s', '--status',
           type=ck.Choice(consts.STATUS, case_sensitive=False),
           help="Choose a status to your task.",
           default=consts.STATUS[3]
           )
def add_task(description, priority, due_date, status):
    """Create a new task"""

    with open('Tasks.json', 'r', encoding='utf-8') as tasks_file_read:
        tasks = json.load(tasks_file_read)

    amount_of_tasks = len(tasks)
    task_id = amount_of_tasks + 1
    priority_upper = priority.upper()
    tasks.append(
        {
            "id": task_id,
            "description": f"{description}",
            "priority": f"{priority_upper}",
            "due_date": f"{due_date}",
            "status": ""
        }
    )
    
    with open('Tasks.json', 'w', encoding='utf-8') as tasks_file_write:
        json.dump(tasks, tasks_file_write, indent=2)

    return tasks[-1]


def view_tasks():
    """View all your tasks"""
    with open('Tasks.json', 'r', encoding='utf-8') as tasks_file:
        tasks = json.load(tasks_file)

    for task in tasks:
        print(task)


if __name__ == '__main__':
    daily_tasks()