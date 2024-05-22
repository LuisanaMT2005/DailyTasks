import json
from datetime import datetime

import click as ck
from daily_tasks.commands import utilities


@ck.command
@ck.option('-d', '--description',
           required=True,
           type=ck.STRING,
           help="Describe your task.")
@ck.option('-p', '--priority',
           type=ck.Choice(utilities.PRIORITIES,
                          case_sensitive=False),
           help="Choose a priority to your task.",
           default=utilities.PRIORITIES[3])
@ck.option('-dd', '--due-date',
           type=ck.DateTime(formats=utilities.DUE_DATE_FORMAT),
           help="Set a due date to your task.",
           default=utilities.get_due_date_default_value())
@ck.option('-s', '--status',
           type=ck.Choice(utilities.STATUS,
                          case_sensitive=False),
           help="Choose a status to your task.",
           default=utilities.STATUS[3])
@ck.option('-sub', '--sub-task',
           is_flag=True,
           required=False,
           help="Indicate that your task is a subtask.")
@ck.option('-id', '--task-id',
           type=ck.INT,
           required=False,
           help="If your task is a subtask, pass the task id it belongs to.")
@ck.option('--tasks-file-path',
           hidden=True,
           required=False,
           type=ck.STRING,
           default=utilities.TASKS_FILE_PATH,
           help="This option is ONLY FOR TESTING.")
@ck.option('--subtasks-file-path',
           hidden=True,
           required=False,
           type=ck.STRING,
           default=utilities.SUBTASKS_FILE_PATH,
           help="This option is ONLY FOR TESTING.")
def add(description: str, priority: str,
        due_date: datetime, status: str,
        sub_task: bool, task_id: int,
        tasks_file_path: str=utilities.TASKS_FILE_PATH,
        subtasks_file_path: str=utilities.SUBTASKS_FILE_PATH) -> None:
    """Create a new task or subtask."""
    if sub_task is False: # Add a new task
        # Read tasks.json file
        try:
            with open(tasks_file_path, 'r', encoding='utf-8') as tasks_file_read:
                tasks: list = json.load(tasks_file_read)
        except json.decoder.JSONDecodeError:
            tasks: list = []

        # Get a new id for the new task
        if tasks == []:
            new_id = 1
        else:
            new_id = tasks[-1]['id'] + 1

        priority_upper, status_capitalize, due_date_formatted = utilities.format_priority_status_and_due_date(priority, status, due_date)

        tasks.append(
            {
                "id": new_id,
                "description": f"{description}",
                "priority": f"{priority_upper}",
                "due_date": f"{due_date_formatted}",
                "status": f"{status_capitalize}",
                "subtasks": []
            }
        )

        # Write down the modified array of tasks
        with open(tasks_file_path, 'w', encoding='utf-8') as tasks_file_write:
            json.dump(tasks, tasks_file_write, indent=2)
    else: # Add a new subtask
        # Read de subtasks.json file
        try:
            with open(subtasks_file_path, 'r', encoding='utf-8') as tasks_file_read:
                subtasks: list = json.load(tasks_file_read)
        except json.decoder.JSONDecodeError:
            subtasks: list = []

        # Get a new id for the new subtask
        if subtasks == []:
            new_id = 1
        else:
            new_id = subtasks[-1]['id'] + 1

        # Read the tasks.json file
        with open(tasks_file_path, 'r', encoding='utf-8') as tasks_file_read:
            tasks: list = json.load(tasks_file_read)

        # Get the task which new subtask will belongs to
        for task in tasks:
            if task['id'] == task_id:
                extracted_task: dict = task
                break
            raise ValueError("A task with the passed id doesn't exist.")

        # Add new subtask id to property 'subtasks' of task (task which the new subtask belongs to)
        try:
            sub_tasks_of_extracted_task: list = extracted_task['subtasks']
            sub_tasks_of_extracted_task.append(new_id)
        except KeyError:
            extracted_task.update(
                {"subtasks": [new_id]}
            )

        priority_upper, status_capitalize, due_date_formatted = utilities.format_priority_status_and_due_date(priority, status, due_date)

        subtasks.append(
            {
                "id": new_id,
                "description": f"{description}",
                "priority": f"{priority_upper}",
                "due_date": f"{due_date_formatted}",
                "status": f"{status_capitalize}",
                "subtask_belongs": extracted_task['id']
            }
        )

        # Write down the modified array of subtasks
        with open(subtasks_file_path, 'w', encoding='utf-8') as sub_tasks_file_write:
            json.dump(subtasks, sub_tasks_file_write, indent=2)

        # Write down the modified array of tasks
        with open(tasks_file_path, 'w', encoding='utf-8') as tasks_file_write:
            json.dump(tasks, tasks_file_write, indent=2)


@ck.command
@ck.option('--tasks-file-path',
           hidden=True,
           required=False,
           type=ck.STRING,
           default=utilities.TASKS_FILE_PATH,
           help="This option is ONLY FOR TESTING.")
@ck.option('--subtasks-file-path',
           hidden=True,
           required=False,
           type=ck.STRING,
           default=utilities.SUBTASKS_FILE_PATH,
           help="This option is ONLY FOR TESTING.")
def view(tasks_file_path: str=utilities.TASKS_FILE_PATH,
         subtasks_file_path: str=utilities.SUBTASKS_FILE_PATH) -> None:
    """View all your tasks and subtasks."""
    with open(tasks_file_path, 'r', encoding='utf-8') as tasks_file:
        tasks = json.load(tasks_file)

    with open(subtasks_file_path, 'r', encoding='utf-8') as subtasks_file:
        subtasks = json.load(subtasks_file)

    for task in tasks:
        utilities.print_tasks(task['id'], task['description'],
                              task['priority'], task['due_date'],
                              task['status'])
        for subtask in subtasks:
            if subtask['subtask_belongs'] == task['id']:
                utilities.print_subtasks(subtask['id'], subtask['description'],
                                         subtask['priority'], subtask['due_date'],
                                         subtask['status'])
