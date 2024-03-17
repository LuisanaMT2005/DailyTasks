from datetime import datetime
import json


def filter_tasks_by_priority(priority):
    """Filter your tasks by priority."""
    with open('Tasks.json', 'r', encoding='utf-8') as reading_tasks_file:
        tasks = json.load(reading_tasks_file)

    priority_upper = priority.upper()

    for task in tasks:
        if task['priority'] == priority_upper:
            print(task)


def filter_tasks_by_due_date(due_date):
    """Filter your tasks by due date."""
    with open('Tasks.json', 'r', encoding='utf-8') as reading_tasks_file:
        tasks = json.load(reading_tasks_file)

    due_date_date_object = due_date.date()

    for task in tasks:
        if task['due_date'] == due_date_date_object:
            print(task)


def filter_tasks_by_status(status):
    """Filter your tasks by status."""
    with open('Tasks.json', 'r', encoding='utf-8') as reading_tasks_file:
        tasks = json.load(reading_tasks_file)

    status_capitalize = status.capitalize()
    for task in tasks:
        if task['status'] == status_capitalize:
            print(task)

