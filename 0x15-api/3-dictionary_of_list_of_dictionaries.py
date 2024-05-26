#!/usr/bin/python3
"""
Python script to export data in the JSON format.
"""
import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    content = requests.get(url + "users")
    users = content.json()

    data = {}
    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        params = {"userId": user_id}
        todos = requests.get(url + "todos", params=params).json()

        user_tasks = [{'username': username,
                       'task': todo.get('title'),
                       'completed': todo.get('completed')
                      } for todo in todos]

        data.update({user_id: user_tasks})

    with open('todo_all_employees.json', 'w', encoding='utf-8') as f:
        json.dump(data, f)
