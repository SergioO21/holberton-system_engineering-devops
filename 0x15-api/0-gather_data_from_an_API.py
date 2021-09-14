#!/usr/bin/python3
"""Script that, using this REST API, for a given employee ID,
 returns information about his/her TODO list progress"""

import requests
from sys import argv

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    e_id = argv[1]
    user = requests.get(url + 'users/' + e_id).json()
    tasks = requests.get(url + 'todos/', params={'userId': e_id}).json()
    name = user.get("name")

    complete_task = 0
    for task in tasks:
        if task.get("completed") is True:
            complete_task += 1

    completed_task = [(i) for i in tasks if i.get("completed") is True]

    print('Employee {} is done with tasks({}/{}):'
          .format(name, complete_task, len(tasks)))

    for task in completed_task:
        print("\t", task["title"])
