#!/usr/bin/python3
"""lists progress of employee's tasks through REST API in json"""

if __name__ == "__main__":
    import csv
    import json
    import sys
    import urllib.request

    data = {}
    my_list = []

    y = urllib.request.urlopen('https://jsonplaceholder.typicode.com/users/')
    user = json.loads(y.read())
    for i in user:
        username = i.get('username')
        user_id = i.get('id')

        x = urllib.request.urlopen('https://jsonplaceholder.typicode.com/todos/')
        todo = json.loads(x.read())
        for j in todo:
            if j.get('userId') == int(user_id):
                tmp = {}
                status = j.get("completed")
                title = j.get("title")
                tmp["task"] = title
                tmp["completed"] = status
                tmp["username"] = username
                my_list.append(tmp)
        x.close()
    y.close()

    data[user_id] = my_list

    with open('todo_all_employees.json', 'w') as f:
        json.dump(data, f)
