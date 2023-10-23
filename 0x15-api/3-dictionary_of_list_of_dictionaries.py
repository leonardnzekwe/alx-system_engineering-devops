#!/usr/bin/python3
"""API Request For All Employees Module"""
import json
import requests


def main():
    try:
        users_response = requests.get(
            "https://jsonplaceholder.typicode.com/users"
        )
        todos_response = requests.get(
            "https://jsonplaceholder.typicode.com/todos"
        )

        if (
            users_response.status_code == 200
            and todos_response.status_code == 200
        ):
            users = users_response.json()
            todos = todos_response.json()

            user_tasks = {}

            for user in users:
                user_id = user.get("id")
                username = user.get("username")
                user_tasks[user_id] = []

                for task in todos:
                    if task.get("userId") == user_id:
                        user_tasks[user_id].append({
                            "username": username,
                            "task": task.get("title"),
                            "completed": task.get("completed")
                        })

            with open("todo_all_employees.json", "w") as json_file:
                json.dump(user_tasks, json_file)
    except Exception as err:
        print(f"Error: {err}")


if __name__ == "__main__":
    main()
