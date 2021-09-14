#!/usr/bin/python3
""" Returns information about his/her TODO list progress. """

import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    TOTAL_NUMBER_OF_TASKS = len(
        requests.get(url + "todos/", params={"userId": argv[1]}).json())
    NUMBER_OF_DONE_TASKS = requests.get(
        url + "todos", params={"userId": argv[1], "completed": "true"}).json()
    EMPLOYEE_NAME = requests.get(
        url + "users/" + argv[1]).json()
    EMPLOYEE_NAME = EMPLOYEE_NAME.get("name")

    print("Employee {} is done with tasks({}/{}):".format(
        EMPLOYEE_NAME, len(NUMBER_OF_DONE_TASKS), TOTAL_NUMBER_OF_TASKS))

    for task in NUMBER_OF_DONE_TASKS:
        print("\t {}".format(task["title"]))