
import json

def load_expenses():
    try:
        file = open("expenses.json", "r")
        expenses = json.load(file)
        file.close()
        return expenses

    except FileNotFoundError:
        return []


def save_expenses(expenses):
    file = open("expenses.json", "w")
    json.dump(expenses, file, indent=2)
    file.close()


def show_expenses(expenses):
    for expense in expenses:
        print("Title:", expense["title"])
        print("Amount:", expense["amount"])
        print("Category:", expense.get("category", "Not set"))
        print("Date:", expense.get("date", "Not set"))
        print("Priority:", expense.get("priority", "Not set"))
        
