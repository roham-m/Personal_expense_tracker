
from expenses import load_expenses, save_expenses, show_expenses
from dotenv import load_dotenv
import os

load_dotenv()

name = input("Enter your name: ")
print("Welcome", name)

admin = input("Do you want to enter admin mode? (yes/no): ")

if admin == "yes":
    password = input("Enter admin password: ")

    if password == os.getenv("EXPENSE_TRACKER_ADMIN_PASSWORD"):
        print("Admin login successful!")
    else:
        print("Wrong password!")

expenses = load_expenses()

print("Previous Expenses:")
show_expenses(expenses)

count = int(input("How many expenses? "))

for i in range(count):
    title = input("Enter expense title: ")

    while title == "":
        print("Title cannot be empty!")
        title = input("Enter expense title: ")

    while True:
        try:
            amount = float(input("Enter amount: "))

            if amount > 0:
                break

            print("Amount must be positive!")

        except ValueError:
            print("Invalid amount!")

    category = input("Enter category: ")
    date = input("Enter date (YYYY-MM-DD): ")

    while True:
        priority = input("Enter priority (low/medium/hard): ").lower()

        if priority == "low" or priority == "medium" or priority == "hard":
            break

        print("Invalid priority! Try again.")

    expense = {
        "title": title,
        "amount": amount,
        "category": category,
        "date": date,
        "priority": priority
    }

    expenses.append(expense)

save_expenses(expenses)

print("All Expenses:")
show_expenses(expenses)
