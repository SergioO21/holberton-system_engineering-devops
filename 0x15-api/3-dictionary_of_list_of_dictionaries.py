#!/usr/bin/python3
"""Dictionary of list of dictionaries"""
import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    counter = len(requests.get(url + "users").json())
    data = {}
    full_data = {}
    for i in range(0, counter):
        user = requests.get(url + "users/" + str(i + 1))
        todo_keys = {"userId": str(i + 1)}
        tasks = requests.get("{}todos".format(url), params=todo_keys)
        employee_name = user.json().get("username")
        l_dict = []

        for task in tasks.json():
            l_dict.append(dict(task=task.get("title"),
                               completed=task.get("completed"),
                               username=employee_name))

        data = {(i+1): l_dict}
        full_data.update(data)

        with open('todo_all_employees.json', 'w') as file:
            json.dump(full_data, file)
