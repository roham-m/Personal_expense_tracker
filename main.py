
from expenses import show_expenses

name = input("Enter your name: ")

while name == "":
    print("Name cannot be empty!")
    name = input("Enter your name: ")

print("Welcome", name)

expenses = []

count = int(input("How many expenses? "))

for i in range(count):
    print("\nExpense", i + 1)

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

print("\nAll Expenses:")
show_expenses(expenses)
