#!/usr/bin/python3
"""
Python script to export data in the JSON format.
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = argv[1]

    content = requests.get(url + "users/{}".format(user_id))
    user = content.json()

    params = {"userId": user_id}

    todos_response = requests.get(url + "todos", params=params)
    todos = todos_response.json()

    username = user.get('username')
    json_file = f'{user_id}.json'
    
    data = {user_id: []}

    for todo in todos:
        data[user_id].append({"task": todo.get("title"),
            "completed": todo.get("completed"), 
            "username": username
        })

    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f)
