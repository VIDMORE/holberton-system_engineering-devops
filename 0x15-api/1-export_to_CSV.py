#!/usr/bin/python3
"""This module defines a script that creates a CSV
about the TO DO list progress of a user"""

import csv
import requests
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    filename = f'{user_id}.csv'
    url = "https://jsonplaceholder.typicode.com"

    user = requests.get("{}/users/{}" .format(url, user_id)).json()
    todo_list = requests.get("{}/users/{}/todos" .format(url, user_id)).json()

    with open(filename, 'w') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in todo_list:
            writer.writerow([user_id, user.get('username'),
                             task.get("completed"), task.get("title")])
