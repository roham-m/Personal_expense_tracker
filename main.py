
from expenses import load_expenses, save_expenses
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

for expense in expenses:
    print(expense["name"], expense["price"])

count = int(input("How many expenses? "))

for i in range(count):
    expense_name = input("Enter expense name: ")

    while expense_name == "":
        print("Name cannot be empty!")
        expense_name = input("Enter expense name: ")

    while True:
        try:
            price = float(input("Enter price: "))

            if price > 0:
                break

            print("Price must be positive!")

        except ValueError:
            print("Invalid price!")

    expense = {
        "name": expense_name,
        "price": price
    }

    expenses.append(expense)

save_expenses(expenses)

print("All Expenses:")

for expense in expenses:
    print(expense["name"], expense["price"])