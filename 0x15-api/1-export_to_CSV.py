#!/usr/bin/python3
""" Export data in the CSV format """

import csv
import requests
from sys import argv


def main():
    """ Returns information about his/her TODO list progress """
    url = "https://jsonplaceholder.typicode.com"

    TOTAL_NUMBER_OF_TASKS = requests.get(
        "{}/todos?userId={}".format(url, argv[1])).json()
    NUMBER_OF_DONE_TASKS = len(requests.get(
        "{}/todos?userId={}&completed=true".format(url, argv[1])).json())
    EMPLOYEE_NAME = requests.get(
        "{}/users/{}".format(url, argv[1])).json()["name"]
    USERNAME = requests.get(
        "{}/users/{}".format(url, argv[1])).json()["username"]

    print("Employee {} is done with tasks({}/{}):".format(
        EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, len(TOTAL_NUMBER_OF_TASKS)))

    task_list = []

    for task in TOTAL_NUMBER_OF_TASKS:
        if task["completed"]:
            print("\t {}".format(task["title"]))

        task_list.append([argv[1], USERNAME, task["completed"], task["title"]])

    with open("USER_ID.csv", "w") as file:
        writer = csv.writer(file, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_ALL)

        for row in task_list:
            writer.writerow(row)


if __name__ == "__main__":
    main()
