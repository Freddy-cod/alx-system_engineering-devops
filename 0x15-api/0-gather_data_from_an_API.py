#!/usr/bin/python3
import requests
import sys
'''Yay'''


def get_employee_todo_progress(employee_id):
    """
    Fetches and displays the TODO list progress for a given employee.

    Args:
        employee_id (int): The ID of the employee whose TODO list progress is to be fetched.

    Returns:
        None
    """
    # Base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch employee data
    user_url = f"{base_url}/users/{employee_id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()

    # Fetch todos for the employee
    todos_url = f"{base_url}/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Extract employee name
    employee_name = user_data.get('name')

    # Calculate the number of completed and total tasks
    completed_tasks = [task for task in todos_data if task.get('completed')]
    total_tasks = len(todos_data)
    done_tasks = len(completed_tasks)

    # Display the employee's TODO list progress
    print(f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")

    # Print the titles of completed tasks
    for task in completed_tasks:
        print(f"\t {task.get('title')}")

if __name__ == "__main__":
    # Ensure an employee ID is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    # Fetch and display the TODO progress for the given employee ID
    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Employee ID must be an integer.")
