from datetime import datetime
import json
import click as ck
from daily_tasks.commands import utilities


@ck.command
@ck.option('-sub', '--sub-task',
           is_flag=True,
           required=False,
           help="Indicate that your task is a subtask.")
@ck.option('-id', '--task-id',
           type=ck.INT, required=True,
           help="Task or subtask id that you want modify.")
@ck.option('-d', '--new-description',
           type=ck.STRING, required=False)
@ck.option('-p', '--new-priority',
           type=ck.Choice(utilities.PRIORITIES,
                          case_sensitive=False),
           required=False)
@ck.option('-s', '--new-status',
           type=ck.Choice(utilities.STATUS,
                          case_sensitive=False),
           required=False)
@ck.option('-dd', '--new-due-date',
           type=ck.DateTime(formats=utilities.DUE_DATE_FORMAT),
           required=False)
@ck.option('-b', '--new-subtask-belongs',
           type=ck.INT, required=False)
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
def modify(task_id, new_description,
           new_priority, new_status,
           new_due_date, sub_task,
           new_subtask_belongs,
           tasks_file_path=utilities.TASKS_FILE_PATH,
           subtasks_file_path=utilities.SUBTASKS_FILE_PATH):
    """Modify a task info."""
    if sub_task is False:
        with open(tasks_file_path, 'r', encoding='utf-8') as tasks_file_read:
            tasks = json.load(tasks_file_read)

        for task in tasks:
            if task['id'] == task_id:
                extracted_task = task
                break
            ck.echo("A task with the passed id doesn't exist.")

        task_index = tasks.index(extracted_task)

        if new_description:
            extracted_task['description'] = new_description.capitalize()

        if new_priority:
            new_priority_upper = new_priority.upper()
            extracted_task['priority'] = new_priority_upper

        if new_status:
            new_status_capitalize = new_status.capitalize()
            extracted_task['status'] = new_status_capitalize

        if new_due_date:
            new_due_date_date_object = new_due_date.date()
            new_due_date_formatted = new_due_date_date_object.strftime(utilities.DUE_DATE_FORMAT[0])

            extracted_task['due_date'] = new_due_date_formatted

        tasks.pop(task_index)
        tasks.insert(task_index, extracted_task)

        with open(tasks_file_path, 'w', encoding='utf-8') as tasks_file_write:
            json.dump(tasks, tasks_file_write, indent=2)
    else:
        with open(subtasks_file_path, 'r', encoding='utf-8') as tasks_file_read:
            subtasks = json.load(tasks_file_read)

        for subtask in subtasks:
            if subtask['id'] == task_id:
                extracted_subtask = subtask
                break
            ck.echo("A task with the passed id doesn't exist.")

        subtask_index = subtasks.index(extracted_subtask)

        if new_description:
            extracted_subtask['description'] = new_description.capitalize()

        if new_priority:
            new_priority_upper = new_priority.upper()
            extracted_subtask['priority'] = new_priority_upper

        if new_status:
            new_status_capitalize = new_status.capitalize()
            extracted_subtask['status'] = new_status_capitalize

        if new_due_date:
            new_due_date_date_object = new_due_date.date()
            new_due_date_formatted = new_due_date_date_object.strftime(utilities.DUE_DATE_FORMAT[0])

            extracted_subtask['due_date'] = new_due_date_formatted

        if new_subtask_belongs: # INCOMPLETO
            extracted_subtask['subtask_belongs'] = new_subtask_belongs
            # Cargar las tasks
            # Revisar cada tarea buscando cual tiene el valor de extracted_subtask['subtask_belongs'] como id
            # Entrar a al valor task['subtasks']
            # Eliminar el número que sea igual que el extracted_subtask['id'] de la tarea que se esta modificando

        subtasks.pop(subtask_index)
        subtasks.insert(subtask_index, extracted_subtask)

        with open(subtasks_file_path, 'w', encoding='utf-8') as tasks_file_write:
            json.dump(subtasks, tasks_file_write, indent=2)
