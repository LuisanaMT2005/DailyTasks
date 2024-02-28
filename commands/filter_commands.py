import json


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

