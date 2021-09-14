#!/usr/bin/python3
"""Export to JSON """
import json
import requests
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/" + user_id)
    todo_keys = {"userId": user_id}
    tasks = requests.get("{}todos".format(url), params=todo_keys)
    employee_name = user.json().get("username")
    l_dict = []

    for task in tasks.json():
        l_dict.append(dict(task=task.get("title"),
                           completed=task.get("completed"),
                           username=employee_name))

    data = {argv[1]: l_dict}

    with open('{}.json'.format(user_id), 'w') as file:
        json.dump(data, file)
