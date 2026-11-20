
import json
import os
from datetime import date

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
    category = input("Category: ")

    try:
        amount = float(input("Amount: "))
        if amount <= 0:
            print("Amount must be positive!")
            return
    except ValueError:
        print("Please enter a valid number!")
        return

    expenses.append({
        "name": name,
        "category": category,
        "amount": amount,
        "date": str(date.today())
    })

    save_expenses()
    print("Expense added successfully!")

def show_expenses():
    if not expenses:
        print("No expenses found.")
        return

    total = 0

    for i, expense in enumerate(expenses):
        print(
            i + 1,
            expense["name"],
            expense["category"],
            expense["amount"],
            expense["date"]
        )
        total += expense["amount"]

    print("Total expenses:", total)

def delete_expense():
    show_expenses()

    if not expenses:
        return

    try:
        number = int(input("Enter expense number to delete: "))

        if 1 <= number <= len(expenses):
            removed = expenses.pop(number - 1)
            save_expenses()
            print(removed["name"], "deleted!")
        else:
            print("Invalid expense number!")

    except ValueError:
        print("Enter a valid number!")

def search_expense():
    keyword = input("Enter expense name to search: ").lower()

    found = False

    for expense in expenses:
        if keyword in expense["name"].lower():
            print(expense)
            found = True

    if not found:
        print("No matching expenses found.")

while True:
    print("\n===== EXPENSE TRACKER V2 =====")
    print("1. Add Expense")
    print("2. Show Expenses")
    print("3. Delete Expense")
    print("4. Search Expense")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        show_expenses()
    elif choice == "3":
        delete_expense()
    elif choice == "4":
        search_expense()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")
