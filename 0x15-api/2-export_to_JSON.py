#!/usr/bin/python3
"""This module defines a script that returns a json
about the TO DO list progress of a user"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    tasks = []
    data = {}
    filename = '{}.json'.format(user_id)
    url = "https://jsonplaceholder.typicode.com"

    user = requests.get("{}/users/{}" .format(url, user_id)).json()
    todo_list = requests.get("{}/users/{}/todos" .format(url, user_id)).json()

    for value in todo_list:
        task = {}
        task["task"] = value.get('title')
        task["completed"] = value.get('completed')
        task["username"] = user.get('username')
        tasks.append(task)
    data[user_id] = tasks

    with open(filename, 'w') as f:
        json.dump(data, f)
