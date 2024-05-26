#!/usr/bin/python3
"""
Python script to export data in the CSV format.
"""
import csv
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
    csv_file = f'{user_id}.csv'

    with open(csv_file, 'w', newline='') as f:
        writer = csv.writer(f)
        [writer.writerow(
            [user_id, username, todo.get("completed"), todo.get("title")]
            )for todo in todos]
