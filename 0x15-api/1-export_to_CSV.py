#!/usr/bin/python3
"""API Request and CSV Saving Module"""
import csv
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
                employee_name = employee.get("username")
                employee_tasks = todos_response.json()
                employee_done_tasks = [
                    (
                        task.get("userId"),
                        employee_name,
                        task.get("completed"),
                        task.get("title"),
                    )
                    for task in employee_tasks
                ]
                csv_filename = f"{id}.csv"

                with open(csv_filename, mode="w", newline="") as csv_file:
                    csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
                    csv_writer.writerows(employee_done_tasks)
        except Exception as err:
            print(f"Error: {err}")


if __name__ == "__main__":
    main()
