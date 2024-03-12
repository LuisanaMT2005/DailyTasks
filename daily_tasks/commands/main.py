import click as ck
from daily_tasks.commands.main_commands import create_tasks_file, add_task, view_tasks
from daily_tasks.commands.modification_commands import modify_description, modify_priority, modify_due_date, modify_status


@ck.group
def daily_tasks() -> None:
    """A tasks manager for those who like work from shell."""


daily_tasks.add_command(create_tasks_file)
daily_tasks.add_command(add_task)
daily_tasks.add_command(view_tasks)
daily_tasks.add_command(modify_description)
daily_tasks.add_command(modify_priority)
daily_tasks.add_command(modify_due_date)
daily_tasks.add_command(modify_status)
