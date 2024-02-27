import json

some_data = {
    "name": "Luisana",
    "age": 18,
    "country": "RD",
    "siblings": 1,
    "siblings_name": ["Viannelys"],
    "books": [
        {
            "title": "Harry Potter y la piedra filosofal", 
            "ranking": None
        },
        {
            "title": "Orgullo y prejuicio", 
            "ranking": 10
        }
    ]
}

with open('user_data.json', 'w', encoding='utf-8') as file:
    file.write(json.dumps(some_data, indent=2))

with open('user_data.json', 'r', encoding= 'utf-8') as file:
    data = json.loads(file.read())
    print(data['books'][0]['ranking'])
