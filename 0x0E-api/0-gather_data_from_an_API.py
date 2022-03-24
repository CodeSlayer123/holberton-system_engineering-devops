#!/usr/bin/python3
"""lists progress of employee's tasks through REST API"""

if __name__ == "__main__":
    import json
    import sys
    import urllib.request

    user_id = sys.argv[1]
    completed = 0
    tasks = 0
    title = "\t "
    x = urllib.request.urlopen('https://jsonplaceholder.typicode.com/todos/')
    todo = json.loads(x.read())
    for i in todo:
        if i.get('userId') == int(user_id):
            tasks += 1
            if i.get('completed') is True:
                title = title + i['title'] + '\n' + '\t '
                completed += 1
    x.close()

    y = urllib.request.urlopen('https://jsonplaceholder.typicode.com/users/{}'
                               .format(user_id))
    user = json.loads(y.read())
    print("Employee {} is done with tasks ({}/{}):"
          .format(user['name'], completed, tasks))
    print(title[:len(title) - 3])
    y.close()
