from os import makedirs
from os.path import lexists, join
import click as ck

from daily_tasks.commands.info_commands import export_tasks, import_tasks
from daily_tasks.commands.main_commands import add, view
from daily_tasks.commands.modification_commands import modify
from daily_tasks.commands.removal_commands import delete
from daily_tasks.commands.filter_commands import filter_tasks
from daily_tasks.commands.utilities import DATA_FILES_PATH, TASKS_FILE_PATH, SUBTASKS_FILE_PATH



@ck.group
@ck.version_option(
    package_name='dailytasks',
    prog_name='dailytasks',
)
def daily_tasks() -> None:
    """A tasks manager for those who like work from shell."""
    makedirs(DATA_FILES_PATH, exist_ok=True)
    if lexists(join(DATA_FILES_PATH, TASKS_FILE_PATH)) and lexists(join(DATA_FILES_PATH, SUBTASKS_FILE_PATH)):
        pass
    else:
        with open(TASKS_FILE_PATH, 'w', encoding='utf-8') as tasks_file:
            pass

        with open(SUBTASKS_FILE_PATH, 'w', encoding='utf-8') as subtasks_file:
            pass


daily_tasks.add_command(add)
daily_tasks.add_command(view)
daily_tasks.add_command(modify)
daily_tasks.add_command(delete)
daily_tasks.add_command(filter_tasks, name='filter')
daily_tasks.add_command(export_tasks, name='export')
daily_tasks.add_command(import_tasks, name='import')
