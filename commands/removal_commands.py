import json


def delete_done_tasks():
    """Delete all your done tasks"""
    with open('Tasks.json', 'r', encoding='utf-8') as reading_tasks_file:
        tasks = json.load(reading_tasks_file)

    for task in tasks:
        if task['status'] == "Done":
            task_index = tasks.index(task)
            tasks.pop(task_index)
    
    with open('Tasks.json', 'w', encoding='utf-8') as writing_tasks_file:
        json.dump(tasks, writing_tasks_file, indent=2)


def delete_task(task_id):
    """Delete a task"""
    with open('Tasks.json', 'r', encoding='utf-8') as reading_tasks_file:
        tasks = json.load(reading_tasks_file)

    for task in tasks:
        if task['id'] == task_id:
            task_index = tasks.index(task)
            tasks.pop(task_index)
        else:
            print("No task with the passed id")

    with open('Tasks.json', 'w', encoding='utf-8') as writing_tasks_file:
        json.dump(tasks, writing_tasks_file, indent=2)

