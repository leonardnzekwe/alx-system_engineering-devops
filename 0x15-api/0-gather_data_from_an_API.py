#!/usr/bin/python3
"""API Request Module"""
import requests
from sys import argv


def main():
    """main program for the requests"""
    if len(argv) == 2:
        try:
            id = argv[1]
            users_url = f"https://jsonplaceholder.typicode.com/users/{id}"
            todos_url = (
                f"https://jsonplaceholder.typicode.com/todos/?userId={id}"
            )
            users_response = requests.get(url=users_url)
            todos_response = requests.get(url=todos_url)

            if (
                users_response.status_code == 200
                and todos_response.status_code == 200
            ):
                employee = users_response.json()
                employee_tasks = todos_response.json()
                employee_done_tasks = [
                    task for task in employee_tasks if task.get("completed")
                ]
                first_line = (
                    f"Employee {employee.get('name')} is done with tasks"
                    f"({len(employee_done_tasks)}/{len(employee_tasks)}):"
                )
                print(first_line)
                for task in employee_done_tasks:
                    print("\t", task.get("title"))
        except Exception as err:
            print(f"Error: {err}")


if __name__ == "__main__":
    main()
