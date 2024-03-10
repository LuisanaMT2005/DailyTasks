from click.testing import CliRunner

from daily_tasks.commands.main_commands import view_tasks, add_task, utilities, create_tasks_file

test_task_data_file = 'Tasks_test.json'

def test_create_tasks_file(test_task_data_file):
    runner = CliRunner()
    result = runner.invoke(create_tasks_file, [test_task_data_file])
    assert result.exit_code == 0, f"Command failed: {result.exception}\n{result.output}"


def test_view_tasks(test_task_data_file):
    runner = CliRunner()

    # Using explicit values for each option, matching the utilities module expectations
    description = "Complete unit test"
    priority = "H"  # High priority
    due_date = "2024/03/15"  # Matching the DUE_DATE_FORMAT
    status = "To-do"  # Initial task status

    result = runner.invoke(add_task, [
        '--description', description,
        '--priority', priority,
        '--due-date', due_date,
        '--status', status,
        '--task_file_name', test_task_data_file,
    ])

    # Verifying the command executed successfully
    assert result.exit_code == 0, f"Command failed: {result.exception}\n{result.output}"




