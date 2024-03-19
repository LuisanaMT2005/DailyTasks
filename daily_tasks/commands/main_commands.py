"""Main commands of this CLI"""
import json
from os.path import exists

import click as ck
from daily_tasks.commands import utilities


@ck.command
@ck.option('-d', '--description',
           required=True,
           type=ck.STRING,
           help="Describe your task."
           )
@ck.option('-p', '--priority',
           type=ck.Choice(utilities.PRIORITIES, case_sensitive=False),
           help="Choose a priority to your task.",
           default=utilities.PRIORITIES[3]
           )
@ck.option('-dd', '--due-date',
           type=ck.DateTime(formats=utilities.DUE_DATE_FORMAT),
           help="Set a due date to your task.",
           default=utilities.get_due_date_default_value()
           )
@ck.option('-s', '--status',
           type=ck.Choice(utilities.STATUS, case_sensitive=False),
           help="Choose a status to your task.",
           default=utilities.STATUS[3]
           )
@ck.option('-f', '--file_name',
           hidden=True,
           required=False,
           type=ck.STRING,
           default=utilities.TASKS_FILE_NAME,
           help="Name your task file, take into account that if the file doesn't exist, this command won't create the task."
           )
def add_task(description, priority, due_date, status, file_name=utilities.TASKS_FILE_NAME) -> None: # pylint: disable=unused-argument
    """Create a new task."""
    
    if exists(path=utilities.TASKS_FILE_NAME) is True:
        with open(utilities.TASKS_FILE_NAME, 'r', encoding='utf-8') as tasks_file_read:
            tasks = json.load(tasks_file_read)
    else:
        utilities.create_tasks_file(utilities.TASKS_FILE_NAME)
        with open(utilities.TASKS_FILE_NAME, 'r', encoding='utf-8') as tasks_file_read:
            tasks = json.load(tasks_file_read)

    if tasks == []:
        new_id = 1
    else:
        last_task = tasks[-1]
        last_id = last_task['id']
        new_id = last_id + 1

    priority_upper = priority.upper()
    status_capitalize = status.capitalize()

    due_date_date_obj = due_date.date()
    due_date_formatted = due_date_date_obj.strftime(utilities.DUE_DATE_FORMAT[0])

    tasks.append(
        {
            "id": new_id,
            "description": f"{description}",
            "priority": f"{priority_upper}",
            "due_date": f"{due_date_formatted}",
            "status": f"{status_capitalize}"
        }
    )

    with open(utilities.TASKS_FILE_NAME, 'w', encoding='utf-8') as tasks_file_write:
        json.dump(tasks, tasks_file_write, indent=2)


@ck.command
@ck.option('-f', '--file_name',
           hidden=True,
           required=False,
           type=ck.STRING,
           default=utilities.TASKS_FILE_NAME,
           help="Name your task file, take into account that if the file doesn't exist, this command won't show your tasks."
           )
def view_tasks(file_name=utilities.TASKS_FILE_NAME) -> None: # pylint: disable=unused-argument
    """View all your tasks."""
    with open(utilities.TASKS_FILE_NAME, 'r', encoding='utf-8') as tasks_file:
        tasks = json.load(tasks_file)

    for task in tasks:

        task_id = task['id']
        description = task['description']
        priority = task['priority']
        due_date = task['due_date']
        status = task['status']

        utilities.stylized_tasks_printing(task_id, description, priority, due_date, status)
