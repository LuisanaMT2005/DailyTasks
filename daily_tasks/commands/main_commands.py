"""Main commands of this CLI"""
import json

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
@ck.option('-sub', '--sub-task',
           is_flag=True,
           required=False,
           help="Indicate that your task is a sub-task."
           )
@ck.option('-id', '--task-id',
           type=ck.INT,
           required=False,
           help="Pass task id it belongs to if your task is a sub-task."
           )
@ck.option('-f', '--file-path',
           hidden=True,
           required=False,
           type=ck.STRING,
           default=utilities.TASKS_FILE_PATH,
           help="This option is ONLY FOR TESTING."
           )
def add(description, priority, due_date, status, sub_task, task_id, file_path=utilities.TASKS_FILE_PATH) -> None: # pylint: disable=unused-argument
    """Create a new task."""
    if sub_task is False:
        with open(utilities.TASKS_FILE_PATH, 'r', encoding='utf-8') as tasks_file_read:
            tasks = json.load(tasks_file_read)

        if tasks == []:
            new_id = 1
        else:
            last_task = tasks[-1]
            last_id = last_task['id']
            new_id = last_id + 1

        priority_upper, due_date_formatted, status_capitalize = utilities.format_priority_status_and_due_date(priority, status, due_date)

        tasks.append(
            {
                "id": new_id,
                "description": f"{description}",
                "priority": f"{priority_upper}",
                "due_date": f"{due_date_formatted}",
                "status": f"{status_capitalize}",
                "sub_tasks": []
            }
        )

        with open(utilities.TASKS_FILE_PATH, 'w', encoding='utf-8') as tasks_file_write:
            json.dump(tasks, tasks_file_write, indent=2) 
    else:
        with open(utilities.SUBTASKS_FILE_PATH, 'r', encoding='utf-8') as sub_tasks_file_read:
            sub_tasks: list = json.load(sub_tasks_file_read)

        if sub_tasks == []:
            new_id = 1
        else:
            last_sub_task = sub_tasks[-1]
            last_id = last_sub_task['id']
            new_id = last_id + 1
        

        with open(utilities.TASKS_FILE_PATH, 'r', encoding='utf-8') as tasks_file_read:
            tasks: list = json.load(tasks_file_read)

        for task in tasks:
            if task['id'] == task_id:
                extracted_task: dict = task
                break
            raise Exception("A task with the passed id doesn't exist.") # pylint: disable=broad-exception-raised

        try:
            sub_tasks_of_extracted_task: list = extracted_task['sub_tasks']
            sub_tasks_of_extracted_task.append(new_id)
        except KeyError:
            extracted_task.update(
                {"sub_tasks": [new_id]}
            )

        priority_upper, due_date_formatted, status_capitalize = utilities.format_priority_status_and_due_date(priority, status, due_date)

        sub_tasks.append(
            {
                "id": new_id,
                "description": f"{description}",
                "priority": f"{priority_upper}",
                "due_date": f"{due_date_formatted}",
                "status": f"{status_capitalize}",
                "belongs_task": extracted_task['id']
            }
        )

        with open(utilities.SUBTASKS_FILE_PATH, 'w', encoding='utf-8') as sub_tasks_file_write:
            json.dump(sub_tasks, sub_tasks_file_write, indent=2)

        with open(utilities.TASKS_FILE_PATH, 'w', encoding='utf-8') as tasks_file_write:
            json.dump(tasks, tasks_file_write, indent=2)

@ck.command
@ck.option('-f', '--file-path',
           hidden=True,
           required=False,
           type=ck.STRING,
           default=utilities.TASKS_FILE_PATH,
           help="This option is ONLY FOR TESTING."
           )
def view(file_path=utilities.TASKS_FILE_PATH) -> None: # pylint: disable=unused-argument
    """View all your tasks."""
    with open(utilities.TASKS_FILE_PATH, 'r', encoding='utf-8') as tasks_file:
        tasks = json.load(tasks_file)

    for task in tasks:

        task_id = task['id']
        description = task['description']
        priority = task['priority']
        due_date = task['due_date']
        status = task['status']

        utilities.stylized_tasks_printing(task_id, description, priority, due_date, status)
        #!NOTA: Crear aquí el for de las sub-tareas.
