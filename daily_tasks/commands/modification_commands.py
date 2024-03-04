from datetime import datetime # pylint: disable=unused-import
import json


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

    new_priority_upper = new_priority.upper()
    extracted_task['priority'] = new_priority_upper

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

    new_due_date_date_object = new_due_date.date()

    extracted_task['due_date'] = new_due_date_date_object

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

    new_status_capitalize = new_status.capitalize()
    extracted_task['status'] = new_status_capitalize

    tasks.pop(task_index)
    tasks.insert(task_index, extracted_task)

    with open('Tasks.json', 'w', encoding='utf-8') as tasks_file_write:
        json.dump(tasks, tasks_file_write, indent=2)

