expenses = []

def add_expense():
    name = input("Expense name: ")
    amount = float(input("Amount: "))

    expenses.append({
        "name": name,
        "amount": amount
    })

    print("Expense added!")

def show_expenses():
    total = 0

    print("\nYour Expenses:")

    for expense in expenses:
        print(expense["name"], "-", expense["amount"])
        total += expense["amount"]

    print("Total:", total)

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
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")
