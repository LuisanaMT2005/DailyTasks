from click.testing import CliRunner
import pytest

from daily_tasks.commands.main_commands import view, add
from daily_tasks.commands.utilities import TASKS_FILE_PATH_FOR_TESTS, SUBTASKS_FILE_PATH_FOR_TESTS


@pytest.mark.parametrize('description, priority, status, due_date', [
    ("Complete unit test for add task (#1)", "H", "2024/03/15", "To-do"),
    ("Complete unit test for add task (#2)", "M", "2024/05/21", "Done")
])
def test_add_task(description, priority,
                  status, due_date):
    runner = CliRunner()

    description = "Complete unit test"
    priority = "H"
    due_date = "2024/03/15"
    status = "To-do"
    test_tasks_data_file = TASKS_FILE_PATH_FOR_TESTS

    result = runner.invoke(add , [
        '--description', description,
        '--priority', priority,
        '--due-date', due_date,
        '--status', status,
        '--tasks-file-path', test_tasks_data_file,
    ])

    assert result.exit_code == 0, f"Command failed: {result.exception}\n{result.output}"


def test_add_subtask():
    runner = CliRunner()

    description = "Complete unit test"
    priority = "H"
    due_date = "2024/03/15"
    status = "To-do"
    test_subtasks_data_file = SUBTASKS_FILE_PATH_FOR_TESTS
    test_tasks_data_file = TASKS_FILE_PATH_FOR_TESTS

    result = runner.invoke(add , [
        '--sub-task',
        '--task-id', 1,
        '--description', description,
        '--priority', priority,
        '--due-date', due_date,
        '--status', status,
        '--subtasks-file-path', test_subtasks_data_file,
        '--tasks-file-path', test_tasks_data_file
    ])

    assert result.exit_code == 0, f"Command failed: {result.exception}\n{result.output}"


def test_view_tasks():
    runner = CliRunner()
    test_tasks_data_file = TASKS_FILE_PATH_FOR_TESTS
    test_subtasks_data_file = SUBTASKS_FILE_PATH_FOR_TESTS
    result = runner.invoke(view , [
        '--tasks-file-path', test_tasks_data_file,
        '--subtasks-file-path', test_subtasks_data_file
    ])

    assert result.exit_code == 0, f"Command failed: {result.exception}\n{result.output}"
