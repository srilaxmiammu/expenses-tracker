import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

FILE_PATH = os.path.join(BASE_DIR, "..", "data", "expenses.json")
FILE_PATH = os.path.abspath(FILE_PATH)

print("FILE PATH =", FILE_PATH)


def load_expenses():

    if not os.path.exists(FILE_PATH):
        return []

    with open(FILE_PATH, "r") as file:
        return json.load(file)


def save_expenses(expenses):

    with open(FILE_PATH, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense():

    expenses = load_expenses()

    name = input("Enter Expense Name: ")
    amount = float(input("Enter Amount: "))

    expenses.append({
        "name": name,
        "amount": amount
    })

    save_expenses(expenses)

    print("Expense Added Successfully!")


def view_expenses():

    expenses = load_expenses()

    if not expenses:
        print("No Expenses Found")
        return

    print("\nExpenses List")

    for index, expense in enumerate(expenses, start=1):

        print(
            f"{index}. "
            f"{expense['name']} - ₹{expense['amount']}"
        )


def delete_expense():

    expenses = load_expenses()

    view_expenses()

    if not expenses:
        return

    choice = int(
        input("Enter Expense Number To Delete: ")
    )

    if 1 <= choice <= len(expenses):

        removed = expenses.pop(choice - 1)

        save_expenses(expenses)

        print(
            f"{removed['name']} Deleted Successfully"
        )

    else:
        print("Invalid Choice")


def total_spending():

    expenses = load_expenses()

    total = sum(
        expense["amount"]
        for expense in expenses
    )

    print(f"Total Spending: ₹{total}")


while True:

    print("\n===== EXPENSE TRACKER =====")

    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Total Spending")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        delete_expense()

    elif choice == "4":
        total_spending()

    elif choice == "5":

        print("Goodbye!")
        break

    else:
        print("Invalid Choice")
