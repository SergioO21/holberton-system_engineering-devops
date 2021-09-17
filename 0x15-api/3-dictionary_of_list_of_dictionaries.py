#!/usr/bin/python3
""" Export data in the JSON format """

import json
import requests


def main():
    """ Returns information about his/her TODO list progress """
    url = "https://jsonplaceholder.typicode.com"

    users = requests.get("{}/users/".format(url)).json()
    task_list = {}

    for user in users:
        user_id = user["id"]
        task_list[user_id] = []
        all_task = requests.get(
                "{}/todos/?userId={}".format(url, user_id)).json()

        for task in all_task:
            task_list[user_id].append({
                "username": user["username"],
                "task": task["title"],
                "completed": task["completed"]
                })

    with open("todo_all_employees.json", "w") as file:
        json.dump(task_list, file)


if __name__ == "__main__":
    main()
