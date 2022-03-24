#!/usr/bin/python3
"""lists progress of employee's tasks through REST API"""
import json
import requests
import sys
if __name__ == "__main__":
    user_id = sys.argv[1]
    completed = 0
    tasks = 0
    title = "\t "

    todo = requests.get("https://jsonplaceholder.typicode.com/todos/").json()
    for i in todo:
        if i.get('userId') == int(user_id):
            tasks += 1
            if i.get('completed') is True:
                title = title + i['title'] + '\n' + '\t '
                completed += 1

    #y = urllib.request.urlopen('https://jsonplaceholder.typicode.com/users/{}'
    #                           .format(user_id))
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(user_id)).json()

    print("Employee {} is done with tasks ({}/{}):"
          .format(user['name'], completed, tasks))
    print(title[:len(title) - 3])
