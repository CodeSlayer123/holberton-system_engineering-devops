#!/usr/bin/python3
"""lists progress of employee's tasks through REST API in json"""

if __name__ == "__main__":
    import json
    import requests

    data = {}
    my_list = []

    user = requests.get('https://jsonplaceholder.typicode.com/users/').json()
    for i in user:
        username = i.get('username')
        user_id = i.get('id')

        todo = requests.get('https://jsonplaceholder.typicode.com/todos/').json()
        for j in todo:
            if j.get('userId') == int(user_id):
                tmp = {}
                status = j.get("completed")
                title = j.get("title")
                tmp["task"] = title
                tmp["completed"] = status
                tmp["username"] = username
                my_list.append(tmp)
        data[user_id] = my_list

    with open('todo_all_employees.json', 'w') as f:
        json.dump(data, f)
