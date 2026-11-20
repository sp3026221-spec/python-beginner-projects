import json
import os

FILE = "expenses.json"

def load_expenses():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

def save_expenses():
    with open(FILE, "w") as f:
        json.dump(expenses, f, indent=4)

expenses = load_expenses()

def add_expense():
    name = input("Expense name: ")
    amount = float(input("Amount: "))

    expenses.append({
        "name": name,
        "amount": amount
    })

    save_expenses()
    print("Expense saved successfully!")

def show_expenses():
    total = 0

    for expense in expenses:
        print(expense["name"], "-", expense["amount"])
        total += expense["amount"]

    print("Total expenses:", total)

while True:
    print("\n1. Add Expense")
    print("2. Show Expenses")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        show_expenses()
    elif choice == "3":
        break
    else:
        print("Invalid choice!")