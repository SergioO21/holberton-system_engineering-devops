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

    with open("{}.csv".format(argv[1]), "w") as file:
        writer = csv.writer(file, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_ALL)

        for task in TOTAL_NUMBER_OF_TASK:
            writer.writerow(
                    [argv[1], USERNAME, task["completed"], task["title"]])


if __name__ == "__main__":
    main()
