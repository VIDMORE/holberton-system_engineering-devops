#!/usr/bin/python3
"""This module defines a script that returns a json
about the TO DO list progress of all users"""

import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    users = requests.get("{}/users/".format(url)).json()
    data = {}
    for user in users:
        tasks = []
        user_id = user.get('id')
        todo_list = requests.get('{}/users/{}/todos'
                                 .format(url, user_id)).json()
        for value in todo_list:
            task = {}
            task["username"] = user.get('username')
            task["task"] = value.get('title')
            task["completed"] = value.get('completed')
            tasks.append(task)
        data[user_id] = tasks
    with open("todo_all_employees.json", 'w') as f:
        json.dump(data, f)
