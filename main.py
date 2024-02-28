import json


#TODO: Modularizar las funciones.
#TODO: Leer los errores que se pueden generar usando el modulo JSON e intentar generar los errores apropósito durante el testing para ver si se generan, y manejarlos (try...except) si ocurren.
#TODO: Integrar el modulo Click para la interfaz de uso (Integrar la clase datetime de el modulo datetime para la due_date).

tasks_structure = {
    "id": "",
    "description": "",
    "priority": "",
    "due_date": "",
    "status": ""
}

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


def modify_description(task_id, new_description):
    """Modify description of a task"""
    with open('Tasks.json', 'r', encoding='utf-8') as tasks_file_read:
        tasks = json.load(tasks_file_read)

    for task in tasks:
        if task['id'] == task_id:
            extracted_task = task
            break

    task_index = tasks.index(extracted_task)

    extracted_task['description'] = new_description

    tasks.pop(task_index)
    tasks.insert(task_index, extracted_task)

    with open('Tasks.json', 'w', encoding='utf-8') as tasks_file_write:
        json.dump(tasks, tasks_file_write, indent=2)


def modify_priority(task_id, new_priority):
    """Modify priority of a task"""
    with open('Tasks.json', 'r', encoding='utf-8') as tasks_file_read:
        tasks = json.load(tasks_file_read)

    for task in tasks:
        if task['id'] == task_id:
            extracted_task = task
            break

    task_index = tasks.index(extracted_task)

    extracted_task['priority'] = new_priority

    tasks.pop(task_index)
    tasks.insert(task_index, extracted_task)

    with open('Tasks.json', 'w', encoding='utf-8') as tasks_file_write:
        json.dump(tasks, tasks_file_write, indent=2)


def modify_due_date(task_id, new_due_date):
    """Modify due date of a task"""
    with open('Tasks.json', 'r', encoding='utf-8') as tasks_file_read:
        tasks = json.load(tasks_file_read)

    for task in tasks:
        if task['id'] == task_id:
            extracted_task = task
            break

    task_index = tasks.index(extracted_task)

    extracted_task['due_date'] = new_due_date

    tasks.pop(task_index)
    tasks.insert(task_index, extracted_task)

    with open('Tasks.json', 'w', encoding='utf-8') as tasks_file_write:
        json.dump(tasks, tasks_file_write, indent=2)


def modify_status(task_id, new_status):
    """Modify status of a task"""
    with open('Tasks.json', 'r', encoding='utf-8') as tasks_file_read:
        tasks = json.load(tasks_file_read)

    for task in tasks:
        if task['id'] == task_id:
            extracted_task = task
            break

    task_index = tasks.index(extracted_task)

    extracted_task['status'] = new_status

    tasks.pop(task_index)
    tasks.insert(task_index, extracted_task)

    with open('Tasks.json', 'w', encoding='utf-8') as tasks_file_write:
        json.dump(tasks, tasks_file_write, indent=2)


def delete_done_tasks():
    """Delete all your done tasks"""
    with open('Tasks.json', 'r', encoding='utf-8') as reading_tasks_file:
        tasks = json.load(reading_tasks_file)

    for task in tasks:
        if task['status'] == "Done" or task['status'] == "done":
            task_index = tasks.index(task)
            tasks.pop(task_index)
    
    with open('Tasks.json', 'w', encoding='utf-8') as writing_tasks_file:
        json.dump(tasks, writing_tasks_file, indent=2)


def delete_task(task_id):
    """Delete a task"""
    with open('Tasks.json', 'r', encoding='utf-8') as reading_tasks_file:
        tasks = json.load(reading_tasks_file)

    for task in tasks:
        if task['id'] == task_id:
            task_index = tasks.index(task)
            tasks.pop(task_index)
        else:
            print("No task with the passed id")

    with open('Tasks.json', 'w', encoding='utf-8') as writing_tasks_file:
        json.dump(tasks, writing_tasks_file, indent=2)


def filter_tasks_by_priority(priority):
    """Filter your tasks by priority"""
    with open('Tasks.json', 'r', encoding='utf-8') as reading_tasks_file:
        tasks = json.load(reading_tasks_file)

    for task in tasks:
        if task['priority'] == priority:
            print(task)


def filter_tasks_by_due_date(due_date):
    """Filter your tasks by due date"""
    with open('Tasks.json', 'r', encoding='utf-8') as reading_tasks_file:
        tasks = json.load(reading_tasks_file)

    for task in tasks:
        if task['due_date'] == due_date:
            print(task)


def filter_tasks_by_status(status):
    """Filter your tasks by status"""
    with open('Tasks.json', 'r', encoding='utf-8') as reading_tasks_file:
        tasks = json.load(reading_tasks_file)

    for task in tasks:
        if task['status'] == status:
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
