#!/usr/bin/python3
# script that, using this REST API, for a given employee ID,
# returns information about his/her TODO list progress.
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    emp_id = argv[1]
    users_url = f'{url}/users/{emp_id}'
    todos_url = f'{url}/users/{emp_id}/todos'

    response = requests.get(users_url)
    users_list = response.json()

    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    completed = []
    for todo in todos:
        if todo.get("completed") is True:
            completed.append(todo.get("title"))

    print("Employee {} is done with({}/{})".format(users_list["name"],
                                                   len(completed), len(todos)))

    for complete in completed:
        print("\t {}".format(complete))
