import json
from commands import filter_commands, modification_commands, removal_commands


#TODO: Leer los errores que se pueden generar usando el modulo JSON e intentar generar los errores apropósito durante el testing para ver si se generan, y manejarlos (try...except) si ocurren.
#TODO: Integrar el modulo Click para la interfaz de uso (Integrar la clase datetime de el modulo datetime para la due_date).


def initialize_tasks_file():
    """Initialize tasks file"""
    with open('Tasks.json', 'w', encoding='utf-8') as tasks_file:
        json.dump([], tasks_file)


def add_task(description, priority, due_date):
    """Add a task"""
    with open('Tasks.json', 'r', encoding='utf-8') as tasks_file_read:
        tasks = json.load(tasks_file_read)

    amount_of_tasks = len(tasks)
    task_id = amount_of_tasks + 1
    tasks.append(
        {
            "id": task_id,
            "description": f"{description}",
            "priority": f"{priority}",
            "due_date": f"{due_date}",
            "status": ""
        }
    )
    
    with open('Tasks.json', 'w', encoding='utf-8') as tasks_file_write:
        json.dump(tasks, tasks_file_write, indent=2)


def view_tasks():
    """View all your tasks"""
    with open('Tasks.json', 'r', encoding='utf-8') as tasks_file:
        tasks = json.load(tasks_file)

    for task in tasks:
        print(task)


### TESTS ###
#initialize_tasks_file()
#add_task("First task", "M", "28/2/2024")
#view_tasks()
#modify_description(1, "Change task")
#modify_priority(1, "H")
#modify_due_date(1, "2024-2-29")
#modify_status(1, "In progress")
#delete_done_tasks()
#delete_task(1)
#filter_tasks_by_priority("H")
#filter_tasks_by_due_date("2024/2/29")
#filter_tasks_by_status("Done")
