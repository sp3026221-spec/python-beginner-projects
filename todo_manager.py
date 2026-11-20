import json
import os

FILE = "tasks.json"

def load_tasks():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks():
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=4)

tasks = load_tasks()

def add_task():
    name = input("Enter task: ")
    tasks.append({
        "name": name,
        "completed": False
    })
    save_tasks()
    print("Task added!")

def show_tasks():
    if not tasks:
        print("No tasks found.")
        return

    for i, task in enumerate(tasks):
        status = "Done" if task["completed"] else "Pending"
        print(i + 1, task["name"], "-", status)

def complete_task():
    show_tasks()
    if not tasks:
        return

    try:
        number = int(input("Task number: "))
        if 1 <= number <= len(tasks):
            tasks[number - 1]["completed"] = True
            save_tasks()
            print("Task completed!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Enter a valid number!")

def delete_task():
    show_tasks()
    if not tasks:
        return

    try:
        number = int(input("Task number to delete: "))
        if 1 <= number <= len(tasks):
            tasks.pop(number - 1)
            save_tasks()
            print("Task deleted!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Enter a valid number!")

while True:
    print("\n===== TO-DO LIST MANAGER =====")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")
      
