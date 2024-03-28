from click.testing import CliRunner
import pytest
import os
from daily_tasks.commands import filter_tasks
from daily_tasks.commands import import_tasks
from daily_tasks.commands import export_tasks


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


def test_subtask_info(tmp_path):
    runner = CliRunner()
    test_file_path = os.path.join(tmp_path, "example.txt")
    with open(test_file_path, 'w') as test_file:
        test_file.write("Test content")

    with runner.isolated_filesystem(temp_dir=tmp_path):
        result = runner.invoke(export_tasks, args=[
            '--export_path', test_file_path  # Pass the file path here
        ])

    assert result.exit_code == 0, f"Command failed:{result.exception}\n{result.output}"

def test_subtask_info(tmp_path):
    runner = CliRunner()
    test_file_path = os.path.join(tmp_path, "example.txt")
    with open(test_file_path, 'w') as test_file:
        test_file.write("Test content")

    with runner.isolated_filesystem(temp_dir=tmp_path):
        result = runner.invoke(import_tasks, args=[
            '--export_path', test_file_path  # Pass the file path here
        ])

    assert result.exit_code == 0, f"Command failed:{result.exception}\n{result.output}"
