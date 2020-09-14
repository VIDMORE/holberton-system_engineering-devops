#!/usr/bin/python3
"""This module defines a script that returns information
about the TO DO list progress of a user"""

import requests
from sys import argv

if __name__ == "__main__":

    user_id = argv[1]
    tasks_completed = 0
    tasks = []

    url = "https://jsonplaceholder.typicode.com"
    user = requests.get("{}/users/{}" .format(url, user_id)).json()
    todo_list = requests.get("{}/users/{}/todos" .format(url, user_id)).json()

    for value in todo_list:
        if value.get('completed') is True:
            tasks_completed += 1
            tasks.append(value.get('title'))
    print("Employee {} is done with tasks({}/{}):".format(
        user.get('name'), tasks_completed, len(todo_list)))
    for task in tasks:
        print("\t {}".format(task))
