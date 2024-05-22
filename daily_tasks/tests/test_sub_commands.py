import os
from click.testing import CliRunner
import pytest

from daily_tasks.commands import filter_tasks, export_tasks, modify, delete
from daily_tasks.commands.utilities import TASKS_FILE_PATH_FOR_TESTS, SUBTASKS_FILE_PATH_FOR_TESTS


def test_modify_task():
    runner = CliRunner()

    task_id = 1
    new_description = "Complete unit test for modify task"
    new_priority = "L"
    new_status = "Done"
    new_due_date = "2024/05/21"
    test_tasks_data_file = TASKS_FILE_PATH_FOR_TESTS
    test_subtaks_data_file = SUBTASKS_FILE_PATH_FOR_TESTS

    result = runner.invoke(modify, [
        '--task-id', task_id,
        '--new-description', new_description,
        '--new-priority', new_priority,
        '--new-status', new_status,
        '--new-due-date', new_due_date,
        '--tasks-file-path', test_tasks_data_file,
        '--subtasks-file-path', test_subtaks_data_file,
    ])
    assert result.exit_code == 0, f"Command failed:{result.exception}\n{result.output}"


def test_modify_subtask():
    runner = CliRunner()

    subtask_id = 1
    new_description = "Complete unit test for modify subtask"
    new_priority = "L"
    new_status = "Done"
    new_due_date = "2024/05/21"
    new_subtask_belongs = 2
    test_tasks_data_file = TASKS_FILE_PATH_FOR_TESTS
    test_subtaks_data_file = SUBTASKS_FILE_PATH_FOR_TESTS

    result = runner.invoke(modify, [
        '--sub-task',
        '--task-id', subtask_id,
        '--new-description', new_description,
        '--new-priority', new_priority,
        '--new-status', new_status,
        '--new-due-date', new_due_date,
        '--new-subtask-belongs', new_subtask_belongs,
        '--tasks-file-path', test_tasks_data_file,
        '--subtasks-file-path', test_subtaks_data_file,
    ])
    assert result.exit_code == 0, f"Command failed:{result.exception}\n{result.output}"


@pytest.mark.skip
def test_subtask_filtering():
    runner = CliRunner()

    priority = "H"
    due_date = "2024/03/15"
    status = "To-do"

    result = runner.invoke(filter_tasks, [
        '--priority', priority,
        '--due-date', due_date,
        '--status', status,
    ])
    assert result.exit_code == 0, f"Command failed: {result.exception}\n{result.output}"


@pytest.fixture()
def tmp_path(tmpdir):
    return tmpdir.strpath


@pytest.mark.skip
def test_subtask_info(tmp_path):
    runner = CliRunner()
    test_file_path = os.path.abspath(os.getcwd())

    with runner.isolated_filesystem(temp_dir=tmp_path):
        result = runner.invoke(export_tasks, args=[
            '--export-path', test_file_path  # Pass the file path here
        ])

    assert result.exit_code == 0, f"Command failed:{result.exception}\n{result.output}"


@pytest.mark.skip
def test_subtask_delete():
    runner = CliRunner()
    task_id = 2
    result = runner.invoke(delete, [
        '--task-id', task_id,
    ])
    assert result.exit_code == 0, f"Command failed:{result.exception}\n{result.output}"
