#!/usr/bin/python3

from sys import argv
import requests


def main():
    """  """
    url = "https://jsonplaceholder.typicode.com"

    task_list = requests.get("{}/todos?userId={}".format(url, argv[1])).json()

    EMPLOYEE_NAME = requests.get("{}/users/{}".format(url, argv[1]))
    EMPLOYEE_NAME = EMPLOYEE_NAME.json()["name"]
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0

    for task in task_list:
        if task["completed"]:
            NUMBER_OF_DONE_TASKS += 1
        TOTAL_NUMBER_OF_TASKS += 1

    print("Employee {} is done with tasks({}/{})".format(
        EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))

    for task in task_list:
        if task["completed"]:
            print("\t {}".format(task["title"]))


if __name__ == "__main__":
    main()
