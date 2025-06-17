import json
import os
from datetime import datetime

# File where tasks will be saved
TASKS_FILE = "tasks.json"

# Load saved tasks from the file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    else:
        return []

# Save tasks into the file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Check if user gave correct date format
def is_valid_date(date_text):
    try:
        datetime.strptime(date_text, "%Y-%m-%d")
        return True
    except ValueError:
        return False

# Add a new task
def add_task(tasks):
    title = input("Enter task name: ").strip()

    # Ask for deadline 
    while True:
        deadline = input("Enter deadline (YYYY-MM-DD): ").strip()
        if is_valid_date(deadline):
            break
        else:
            print("Please enter date in correct format like 2025-06-15")

    new_task = {
        "title": title,
        "status": "pending",
        "deadline": deadline
    }

    tasks.append(new_task)
    print("Task added!")

# Show all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks to show!")
        return

    print("\n--- Your Tasks ---")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['title']} [{task['status']}] - Deadline: {task['deadline']}")
    print()

# Mark a task as done
def mark_done(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= num < len(tasks):
            tasks[num]["status"] = "done"
            print("Task marked as done!")
        else:
            print("Invalid number!")
    except ValueError:
        print("Please enter a number.")

# Delete a task
def delete_task(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to delete: ")) - 1
        if 0 <= num < len(tasks):
            removed = tasks.pop(num)
            print(f"Task '{removed['title']}' deleted!")
        else:
            print("Invalid number!")
    except ValueError:
        print("Please enter a number.")

# Main menu
def main():
    tasks = load_tasks()

    while True:
        print("\n--- To-Do List Menu ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose option (1-5): ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Tasks saved. Bye!")
            break
        else:
            print("Please enter a valid number between 1 to 5.")

# Start 
if __name__ == "__main__":
    main()
