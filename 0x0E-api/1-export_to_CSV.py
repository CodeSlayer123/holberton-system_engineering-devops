#!/usr/bin/python3
"""lists progress of employee's tasks through REST API in csv"""

if __name__ == "__main__":
    import csv
    import json
    import sys
    import urllib.request

    user_id = sys.argv[1]
    completed = 0
    tasks = 0
    rows = [[]]
    x = urllib.request.urlopen('https://jsonplaceholder.typicode.com/todos/')
    todo = json.loads(x.read())
    for i in todo:
        if i.get('userId') == int(user_id):
            tasks += 1
            y = urllib.request.urlopen('https://jsonplaceholder.typicode.com/users/{}'.format(user_id))
            user = json.loads(y.read())
            status = i.get('completed')
            title = i.get('title')
            username = user.get('username')
            rows.append([user_id, username, status, title])
            y.close()

    x.close()

    with open('{}.csv'.format(user_id), 'w') as f:
        csvwriter = csv.writer(f, quoting=csv.QUOTE_ALL)
       # csvwriter.writerow(fields)
        csvwriter.writerows(rows)
