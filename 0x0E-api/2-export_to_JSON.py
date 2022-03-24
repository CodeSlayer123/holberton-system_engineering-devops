#!/usr/bin/python3
"""lists progress of employee's tasks through REST API in json"""

if __name__ == "__main__":
    import json
    import requests
    import sys

    user_id = sys.argv[1]
    data = {}
    my_list = []

    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(user_id)).json()
    username = user.get('username')

    todo = requests.get('https://jsonplaceholder.typicode.com/todos/').json()
    for i in todo:
        if i.get('userId') == int(user_id):
            tmp = {}
            status = i.get("completed")
            title = i.get("title")
            tmp["task"] = title
            tmp["completed"] = status
            tmp["username"] = username
            my_list.append(tmp)
    data[user_id] = my_list

    with open('{}.json'.format(user_id), 'w') as f:
        json.dump(data, f)
