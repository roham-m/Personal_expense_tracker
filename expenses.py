
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
    json.dump(expenses, file)
    file.close()
