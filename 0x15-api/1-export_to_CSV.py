#!/usr/bin/python3
"""script to export data in the CSV format"""


if __name__ == "__main__":
    import requests
    from sys import argv
    import csv
    url = "https://jsonplaceholder.typicode.com/"
    user_id = argv[1]
    user = requests.get(url + "users/{}".format(user_id)).json()
    tasks = requests.get(url + "todos/?userId={}".format(user_id)).json()

    with open("{}.csv".format(user_id), "w") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow([user_id, user["username"],
                            task["completed"], task["title"]])