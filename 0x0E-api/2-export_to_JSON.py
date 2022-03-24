#!/usr/bin/python3
"""lists progress of employee's tasks through REST API in json"""

if __name__ == "__main__":
    import json
    import sys
    import urllib.request

    user_id = sys.argv[1]
    data = {}
    my_list = []

    y = urllib.request.urlopen('https://jsonplaceholder.typicode.com/users/{}'.format(user_id))
    user = json.loads(y.read())
    username = user.get('username')
    y.close()

    x = urllib.request.urlopen('https://jsonplaceholder.typicode.com/todos/')
    todo = json.loads(x.read())
    for i in todo:
        if i.get('userId') == int(user_id):
            tmp = {}
            status = i.get("completed")
            title = i.get("title")
            tmp["task"] = title
            tmp["completed"] = status
            tmp["username"] = username
            my_list.append(tmp)
    x.close()
    data[user_id] = my_list

    with open('{}.json'.format(user_id), 'w') as f:
        json.dump(data, f)
