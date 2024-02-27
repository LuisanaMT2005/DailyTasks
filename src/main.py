import json


#TODO: Leer los errores que se pueden generar usando el modulo JSON e intentar generar los errores apropósito durante el testing para ver si se generan, y manejarlos (try...except) si ocurren.
#TODO: Integrar la clase date de el modulo datetime para la due_date.
#TODO: Integrar el modulo Click para la interfaz de uso.

tasks_structure = {
    "task_n": {
        "description": "",
        "priority": "",
        "due_date": "",
        "status": ""
    }
}

def add_tasks(description, priority, due_date, status):
    with open('user_tasks.json', 'r', encoding= 'utf-8') as tasks_file:
        try:
            tasks = json.loads(tasks_file.read())
            amount_of_tasks = len(tasks.keys())
            task = {
            "task_%d" % (amount_of_tasks + 1): {
                "description": "%s" % (description),
                "priority": "%s" % (priority),
                "due_date": "%s" % (due_date),
                "status": "%s" % (status)
                }
            }
            new_tasks_file = tasks.update(task)
            tasks_file_w_mode = open('user_tasks.json', 'w', encoding= 'utf-8')
            tasks_file_w_mode.write(json.dumps(new_tasks_file, indent=2))
            tasks_file_w_mode.close()
        except AttributeError:
            tasks_file_a_mode = open('user_tasks.json', 'a', encoding= 'utf-8')
            tasks_file_a_mode.write(json.dumps(task, indent=2))

         #!TODO: Ver como puedo ampliar el objeto JSON, probar cargando el archivo de tareas y luego actualizar el diccionario con el método .update.

add_tasks("First task", "M", "28/2/2024", "TO-DO")
