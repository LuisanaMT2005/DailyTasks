from click.testing import CliRunner
import pytest
import os
from daily_tasks.commands.main_commands import view, add
from daily_tasks.commands import filter_tasks, info_commands


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
    # Using tmpdir fixture provided by pytest
    return tmpdir.strpath


def test_subtask_info(tmp_path):
    runner = CliRunner()
    test_file_path = os.path.join(tmp_path, "example.txt")
    # Create a test file within the temporary directory
    with open(test_file_path, 'w') as test_file:
        test_file.write("Test content")

    with runner.isolated_filesystem(temp_dir=tmp_path):
        result = runner.invoke(info_commands, args=[
            '--export_path', test_file_path  # Pass the file path here
        ])

    assert result.exit_code == 0, f"Command failed:{result.exception}\n{result.output}"
