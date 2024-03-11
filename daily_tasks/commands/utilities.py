"""Utilities"""
from datetime import datetime
from os import listdir


DUE_DATE_FORMAT = ['%Y/%m/%d']
PRIORITIES = ['H', 'M', 'L', ' ']
STATUS = ['To-do', 'In progress', 'Done', ' ']

def get_due_date_default_value() -> str:
    """Get default value for due_date parameter"""
    today_datetime_obj = datetime.today()
    today_date_obj = today_datetime_obj.date()
    today_date_obj_formatted = today_date_obj.strftime(DUE_DATE_FORMAT[0])
    today_date_str_formatted = str(today_date_obj_formatted)

    return today_date_str_formatted

def check_if_a_json_file_exist() -> str:
    files = listdir('./daily_tasks/')

    for file in files:
        if file.endswith('.json'):
            tasks_file = file
            break
        continue

    return tasks_file
