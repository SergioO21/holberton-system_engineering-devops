#!/usr/bin/python3
"""Export to CSV"""
import csv
import requests
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/" + user_id)
    todo_keys = {"userId": user_id}
    tasks = requests.get("{}todos".format(url), params=todo_keys)
    employee_name = user.json().get("username")

    with open('{}.csv'.format(user_id), mode='w') as csv_file:
        writer = csv.writer(csv_file,
                            delimiter=',',
                            quotechar='"',
                            quoting=csv.QUOTE_ALL)

        for task in tasks.json():
            writer.writerow([user_id,
                             employee_name,
                             task.get('completed'),
                             task.get('title')])
