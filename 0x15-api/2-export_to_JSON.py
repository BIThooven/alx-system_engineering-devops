#!/usr/bin/python3
"""exporting data to a json"""
import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    response = requests.get(url)
    user = response.json()
    url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(user_id)
    response = requests.get(url)
    todos = response.json()
    tasks = []
    for task in todos:
        task_dict = {}
        task_dict['task'] = task.get('title')
        task_dict['completed'] = task.get('completed')
        task_dict['username'] = user.get('username')
        tasks.append(task_dict)
    json_dict = {}
    json_dict[user_id] = tasks
    with open('{}.json'.format(user_id), 'w') as f:
        json.dump(json_dict, f)
