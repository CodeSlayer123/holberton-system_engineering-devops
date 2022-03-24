#!/usr/bin/python3
"""lists progress of employee's tasks through REST API in csv"""

if __name__ == "__main__":
    import csv
    import json
    import requests
    import sys

    user_id = sys.argv[1]
    completed = 0
    tasks = 0
    rows = [[]]
    todo = requests.get('https://jsonplaceholder.typicode.com/todos/').json()
    for i in todo:
        if i.get('userId') == int(user_id):
            tasks += 1
            user = requests.get(
                'https://jsonplaceholder.typicode.com/users/{}'
                .format(user_id)).json()
            status = i.get('completed')
            title = i.get('title')
            username = user.get('username')
            rows.append([user_id, username, status, title])

    with open('{}.csv'.format(user_id), 'w') as f:
        csvwriter = csv.writer(f, quoting=csv.QUOTE_ALL)
        csvwriter.writerows(rows)
