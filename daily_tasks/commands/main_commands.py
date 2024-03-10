"""Main commands of this CLI"""
import json

import click as ck
from daily_tasks.commands import utilities


@ck.command
@ck.option('-f', '--file_name',
           required=True,
           type=ck.STRING,
           help="Name your task file."
           )
def create_tasks_file(file_name) -> None:
    """Create the tasks file (it will be empty)."""
    with open(file_name, 'w', encoding='utf-8') as tasks_file:
        json.dump([], tasks_file)

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
           required=True,
           type=ck.STRING,
           help="Name your task file."
           )
def add_task(description, priority, due_date, status, file_name) -> None:
    """Create a new task"""

    with open(file_name, 'r', encoding='utf-8') as tasks_file_read:
        tasks = json.load(tasks_file_read)

    amount_of_tasks = len(tasks)
    task_id = amount_of_tasks + 1

    priority_upper = priority.upper()
    status_capitalize = status.capitalize()

    due_date_date_obj = due_date.date()
    due_date_formatted = due_date_date_obj.strftime(utilities.DUE_DATE_FORMAT[0])

    tasks.append(
        {
            "id": task_id,
            "description": f"{description}",
            "priority": f"{priority_upper}",
            "due_date": f"{due_date_formatted}",
            "status": f"{status_capitalize}"
        }
    )

    with open('Tasks.json', 'w', encoding='utf-8') as tasks_file_write:
        json.dump(tasks, tasks_file_write, indent=2)


@ck.command
@ck.option('-f', '--file_name',
           required=True,
           type=ck.STRING,
           help="Name your task file."
           )
def view_tasks(file_name) -> None:
    """View all your tasks"""
    with open(file_name, 'r', encoding='utf-8') as tasks_file:
        tasks = json.load(tasks_file)

    for task in tasks:

        task_id = task['id']
        description = task['description']
        priority = task['priority']
        due_date = task['due_date']
        status = task['status']

        if priority == utilities.PRIORITIES[0]:
            if status == utilities.STATUS[0]:
                ck.echo('{}. {} - {} - {} - {}'.format(
                    ck.style(text=task_id, fg='black'),
                    description,
                    ck.style(text=priority, fg='red', bold=True),
                    ck.style(text=status, fg='red'),
                    ck.style(text=due_date, bold=True)
                ))
            elif status == utilities.STATUS[1]:
                ck.echo('{}. {} - {} - {} - {}'.format(
                    ck.style(text=task_id, fg='black'),
                    description,
                    ck.style(text=priority, fg='red', bold=True),
                    ck.style(text=status, fg='yellow'),
                    ck.style(text=due_date, bold=True)
                ))
            else:
                ck.echo('{}. {} - {} - {} - {}'.format(
                    ck.style(text=task_id, fg='black'),
                    description,
                    ck.style(text=priority, fg='red', bold=True),
                    ck.style(text=status, fg='green'),
                    ck.style(text=due_date, bold=True)
                ))
        elif priority == utilities.PRIORITIES[1]:
            if status == utilities.STATUS[0]:
                ck.echo('{}. {} - {} - {} - {}'.format(
                    ck.style(text=task_id, fg='black'),
                    description,
                    ck.style(text=priority, fg='yellow', bold=True),
                    ck.style(text=status, fg='red'),
                    ck.style(text=due_date, bold=True)
                ))
            elif status == utilities.STATUS[1]:
                ck.echo('{}. {} - {} - {} - {}'.format(
                    ck.style(text=task_id, fg='black'),
                    description,
                    ck.style(text=priority, fg='yellow', bold=True),
                    ck.style(text=status, fg='yellow'),
                    ck.style(text=due_date, bold=True)
                ))
            else:
                ck.echo('{}. {} - {} - {} - {}'.format(
                    ck.style(text=task_id, fg='black'),
                    description,
                    ck.style(text=priority, fg='yellow', bold=True),
                    ck.style(text=status, fg='green'),
                    ck.style(text=due_date, bold=True)
                ))
        else:
            if status == utilities.STATUS[0]:
                ck.echo('{}. {} - {} - {} - {}'.format(
                    ck.style(text=task_id, fg='black'),
                    description,
                    ck.style(text=priority, fg='white', bold=True),
                    ck.style(text=status, fg='red'),
                    ck.style(text=due_date, bold=True)
                ))
            elif status == utilities.STATUS[1]:
                ck.echo('{}. {} - {} - {} - {}'.format(
                    ck.style(text=task_id, fg='black'),
                    description,
                    ck.style(text=priority, fg='white', bold=True),
                    ck.style(text=status, fg='yellow'),
                    ck.style(text=due_date, bold=True)
                ))
            else:
                ck.echo('{}. {} - {} - {} - {}'.format(
                    ck.style(text=task_id, fg='black'),
                    description,
                    ck.style(text=priority, fg='white', bold=True),
                    ck.style(text=status, fg='green'),
                    ck.style(text=due_date, bold=True)
                ))