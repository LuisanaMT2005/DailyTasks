from click.testing import CliRunner

from daily_tasks.commands.main_commands import view, add
from daily_tasks.commands.utilities import TASKS_FILE_PATH_FOR_TESTS, SUBTASKS_FILE_PATH_FOR_TESTS


def test_add_task():
    runner = CliRunner()

    description = "Complete unit test"
    priority = "H"
    due_date = "2024/03/15"
    status = "To-do"
    test_task_data_file = TASKS_FILE_PATH_FOR_TESTS

    result = runner.invoke(add , [
        '--description', description,
        '--priority', priority,
        '--due-date', due_date,
        '--status', status,
        '--tasks-file-path', test_task_data_file,
    ])

    assert result.exit_code == 0, f"Command failed: {result.exception}\n{result.output}"


def test_add_subtask():
    runner = CliRunner()

    description = "Complete unit test"
    priority = "H"
    due_date = "2024/03/15"
    status = "To-do"
    test_subtask_data_file = SUBTASKS_FILE_PATH_FOR_TESTS
    test_task_data_file = TASKS_FILE_PATH_FOR_TESTS

    result = runner.invoke(add , [
        '--sub-task',
        '--task-id', 1,
        '--description', description,
        '--priority', priority,
        '--due-date', due_date,
        '--status', status,
        '--subtasks-file-path', test_subtask_data_file,
        '--tasks-file-path', test_task_data_file
    ])

    assert result.exit_code == 0, f"Command failed: {result.exception}\n{result.output}"


def test_view_tasks():
    runner = CliRunner()
    test_task_data_file = TASKS_FILE_PATH_FOR_TESTS
    test_subtask_data_file = SUBTASKS_FILE_PATH_FOR_TESTS
    result = runner.invoke(view , [
        '--tasks-file-path', test_task_data_file,
        '--subtasks-file-path', test_subtask_data_file
    ])

    assert result.exit_code == 0, f"Command failed: {result.exception}\n{result.output}"
