#!/usr/bin/python3
"""API Request and JSON Saving Module"""
import json
import requests
from sys import argv


def main():
    """main program for the requests"""
    if len(argv) == 2:
        try:
            id = argv[1]
            users_response = requests.get(
                f"https://jsonplaceholder.typicode.com/users/{id}"
            )
            todos_response = requests.get(
                f"https://jsonplaceholder.typicode.com/todos/?userId={id}"
            )

            if (
                users_response.status_code == 200
                and todos_response.status_code == 200
            ):
                employee = users_response.json()
                employee_tasks = todos_response.json()
                employee_name = employee.get("username")
                employee_done_tasks = [
                    {
                        "task": task.get("title"),
                        "completed": task.get("completed"),
                        "username": employee_name,
                    }
                    for task in employee_tasks
                ]
                json_filename = f"{id}.json"

                with open(json_filename, "w") as json_file:
                    json.dump({id: employee_done_tasks}, json_file)
        except Exception as err:
            print(f"Error: {err}")


if __name__ == "__main__":
    main()
