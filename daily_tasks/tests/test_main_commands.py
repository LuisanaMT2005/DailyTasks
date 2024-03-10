from click.testing import CliRunner

from daily_tasks.commands.main_commands import view_tasks, add_task, utilities, create_tasks_file


def test_create_tasks_file():
    runner = CliRunner()
    test_task_data_file = 'Tasks_test.json'
    result = runner.invoke(create_tasks_file, ['--file_name', test_task_data_file])
    assert result.exit_code == 0, f"Command failed: {result.exception}\n{result.output}"


def test_add_task():
    runner = CliRunner()

    # Using explicit values for each option, matching the utilities module expectations
    description = "Complete unit test"
    priority = "H"  # High priority
    due_date = "2024/03/15"  # Matching the DUE_DATE_FORMAT
    status = "To-do"  # Initial task status
    test_task_data_file = "Tasks_test.json"

    result = runner.invoke(add_task, [
        '--description', description,
        '--priority', priority,
        '--due-date', due_date,
        '--status', status,
        '--file_name', test_task_data_file,
    ])

    # Verifying the command executed successfully
    assert result.exit_code == 0, f"Command failed: {result.exception}\n{result.output}"




