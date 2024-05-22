from datetime import datetime, date
from os.path import join, dirname, abspath
from os import environ
import click as ck


DUE_DATE_FORMAT = ['%Y/%m/%d']
PRIORITIES = ['H', 'M', 'L', ' ']
STATUS = ['To-do', 'In-progress', 'Done', ' ']

# Productions paths
DATA_FILES_PATH = join(environ.get('APPDATA'), 'dailytasks')
TASKS_FILE_PATH = join(DATA_FILES_PATH, 'tasks.json')
SUBTASKS_FILE_PATH = join(DATA_FILES_PATH, 'subtasks.json')
EXPORTED_TASKS_FILE = 'exported_tasks.json'

# Test paths
DATA_FILES_PATH_FOR_TESTS = join(dirname(dirname(abspath(__file__))),
                                 'data_files')
TASKS_FILE_PATH_FOR_TESTS = join(DATA_FILES_PATH_FOR_TESTS, 'tasks.json')
SUBTASKS_FILE_PATH_FOR_TESTS = join(DATA_FILES_PATH_FOR_TESTS, 'subtasks.json')


def get_due_date_default_value() -> str:
    """Get default value for due_date parameter"""
    return str(datetime.today().date().strftime(DUE_DATE_FORMAT[0]))


def print_tasks(task_id: int, description: str,
                            priority: str, due_date: date,
                            status: str) -> None:
    if priority == PRIORITIES[0]:
        if status == STATUS[0]:
            ck.echo('{}. {} - {} - {} - {}'.format(
                ck.style(text=task_id, fg='white'),
                description,
                ck.style(text=priority, fg='red', bold=True),
                ck.style(text=status, fg='red'),
                ck.style(text=due_date, bold=True)
            ))
        elif status == STATUS[1]:
            ck.echo('{}. {} - {} - {} - {}'.format(
                ck.style(text=task_id, fg='white'),
                description,
                ck.style(text=priority, fg='red', bold=True),
                ck.style(text=status, fg='yellow'),
                ck.style(text=due_date, bold=True)
            ))
        else:
            ck.echo('{}. {} - {} - {} - {}'.format(
                ck.style(text=task_id, fg='white'),
                description,
                ck.style(text=priority, fg='red', bold=True),
                ck.style(text=status, fg='green'),
                ck.style(text=due_date, bold=True)
            ))
    elif priority == PRIORITIES[1]:
        if status == STATUS[0]:
            ck.echo('{}. {} - {} - {} - {}'.format(
                ck.style(text=task_id, fg='white'),
                description,
                ck.style(text=priority, fg='yellow', bold=True),
                ck.style(text=status, fg='red'),
                ck.style(text=due_date, bold=True)
            ))
        elif status == STATUS[1]:
            ck.echo('{}. {} - {} - {} - {}'.format(
                ck.style(text=task_id, fg='white'),
                description,
                ck.style(text=priority, fg='yellow', bold=True),
                ck.style(text=status, fg='yellow'),
                ck.style(text=due_date, bold=True)
            ))
        else:
            ck.echo('{}. {} - {} - {} - {}'.format(
                ck.style(text=task_id, fg='white'),
                description,
                ck.style(text=priority, fg='yellow', bold=True),
                ck.style(text=status, fg='green'),
                ck.style(text=due_date, bold=True)
            ))
    else:
        if status == STATUS[0]:
            ck.echo('{}. {} - {} - {} - {}'.format(
                ck.style(text=task_id, fg='white'),
                description,
                ck.style(text=priority, fg='white', bold=True),
                ck.style(text=status, fg='red'),
                ck.style(text=due_date, bold=True)
            ))
        elif status == STATUS[1]:
            ck.echo('{}. {} - {} - {} - {}'.format(
                ck.style(text=task_id, fg='white'),
                description,
                ck.style(text=priority, fg='white', bold=True),
                ck.style(text=status, fg='yellow'),
                ck.style(text=due_date, bold=True)
            ))
        else:
            ck.echo('{}. {} - {} - {} - {}'.format(
                ck.style(text=task_id, fg='white'),
                description,
                ck.style(text=priority, fg='white', bold=True),
                ck.style(text=status, fg='green'),
                ck.style(text=due_date, bold=True)
            ))


def print_subtasks(task_id: int, description: str,
                            priority: str, due_date: date,
                            status: str) -> None:
    if priority == PRIORITIES[0]:
        if status == STATUS[0]:
            ck.echo('     {}. {} - {} - {} - {}'.format(
                ck.style(text=task_id, fg='white'),
                description,
                ck.style(text=priority, fg='red', bold=True),
                ck.style(text=status, fg='red'),
                ck.style(text=due_date, bold=True)
            ))
        elif status == STATUS[1]:
            ck.echo('     {}. {} - {} - {} - {}'.format(
                ck.style(text=task_id, fg='white'),
                description,
                ck.style(text=priority, fg='red', bold=True),
                ck.style(text=status, fg='yellow'),
                ck.style(text=due_date, bold=True)
            ))
        else:
            ck.echo('     {}. {} - {} - {} - {}'.format(
                ck.style(text=task_id, fg='white'),
                description,
                ck.style(text=priority, fg='red', bold=True),
                ck.style(text=status, fg='green'),
                ck.style(text=due_date, bold=True)
            ))
    elif priority == PRIORITIES[1]:
        if status == STATUS[0]:
            ck.echo('     {}. {} - {} - {} - {}'.format(
                ck.style(text=task_id, fg='white'),
                description,
                ck.style(text=priority, fg='yellow', bold=True),
                ck.style(text=status, fg='red'),
                ck.style(text=due_date, bold=True)
            ))
        elif status == STATUS[1]:
            ck.echo('     {}. {} - {} - {} - {}'.format(
                ck.style(text=task_id, fg='white'),
                description,
                ck.style(text=priority, fg='yellow', bold=True),
                ck.style(text=status, fg='yellow'),
                ck.style(text=due_date, bold=True)
            ))
        else:
            ck.echo('     {}. {} - {} - {} - {}'.format(
                ck.style(text=task_id, fg='white'),
                description,
                ck.style(text=priority, fg='yellow', bold=True),
                ck.style(text=status, fg='green'),
                ck.style(text=due_date, bold=True)
            ))
    else:
        if status == STATUS[0]:
            ck.echo('     {}. {} - {} - {} - {}'.format(
                ck.style(text=task_id, fg='white'),
                description,
                ck.style(text=priority, fg='white', bold=True),
                ck.style(text=status, fg='red'),
                ck.style(text=due_date, bold=True)
            ))
        elif status == STATUS[1]:
            ck.echo('     {}. {} - {} - {} - {}'.format(
                ck.style(text=task_id, fg='white'),
                description,
                ck.style(text=priority, fg='white', bold=True),
                ck.style(text=status, fg='yellow'),
                ck.style(text=due_date, bold=True)
            ))
        else:
            ck.echo('     {}. {} - {} - {} - {}'.format(
                ck.style(text=task_id, fg='white'),
                description,
                ck.style(text=priority, fg='white', bold=True),
                ck.style(text=status, fg='green'),
                ck.style(text=due_date, bold=True)
            ))


def format_priority_status_and_due_date(priority: str, status: str, due_date: datetime) -> tuple:
    priority_upper: str = priority.upper()
    status_capitalize: str = status.capitalize()

    due_date_date_obj: date = due_date.date()
    due_date_formatted: str = due_date_date_obj.strftime(DUE_DATE_FORMAT[0])

    return (priority_upper, status_capitalize, due_date_formatted)
