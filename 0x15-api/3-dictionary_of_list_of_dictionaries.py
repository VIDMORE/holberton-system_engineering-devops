#!/usr/bin/python3
"""This module defines a script that returns a json
about the TO DO list progress of all users"""

import json
import requests

if __name__ == "__main__":
    url = requests.get('https://jsonplaceholder.typicode.com/users/').json()
    data = {}
    for user in url:
        tasks = []
        user_id = user.get('id')
        todo_list = requests.get(
            f'https://jsonplaceholder.typicode.com/users/{user_id}/todos}')
        .json()
        for value in todo_list:
            task = {}
            task["username"] = user.get('username')
            task["task"] = value.get('title')
            task["completed"] = value.get('completed')
            tasks.append(task)
        data[user_id] = tasks
    with open("todo_all_employees.json", 'w') as f:
        json.dump(task_dict, f)
