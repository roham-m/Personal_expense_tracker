**# Expense Tracker**

![Python](https://img.shields.io/badge/python-blue?logo=python&logoColor=white)

A simple expense tracker built with Python.

**## Features**
- add multiple expenses
- display expenses
- save expenses
- load saved expenses
- admin mode

**## Requirements**
- python
- python-dotenv

**## Project Structure**

```text
EXPENSE_TRACKER/
│
├── .env.example
├── .gitignore
├── main.py
├── expenses.py
├── README.md
├── requirements.txt
├── expenses.json
└── images/
```

- `main.py` - main program and user interaction
- `expenses.py` - functions for loading, saving and displaying expenses
- `expenses.json` - stores expense records (created automatically)
- `.env.example` - example environment settings
- `.gitignore` - files that should not be uploaded to Git
- `requirements.txt` - required Python packages
- `images/` - stores project images
- `README.md` - project documentation

**## How It Works**

1. The program asks for the user's name.
2. Previous expenses are loaded from `expenses.json`.
3. The user can choose to enter admin mode.
4. If admin mode is selected, the program asks for a password.
5. The user enters the number of expenses and adds their names and prices.
6. All expenses are displayed.
7. The expenses are saved to `expenses.json`.

**## Installation**

Install the required packages:

```bash
python -m pip install -r requirements.txt
```

**## Environment Setup**

Create a `.env` file in the project folder.

Use `.env.example` as a template.

Add your admin password:

```env
EXPENSE_TRACKER_ADMIN_PASSWORD=your_password_here
```

Replace `your_password_here` with your own test password.

**## Run the Program**

Run the main file:

```bash
python main.py
```

**## Troubleshooting**

**1. FileNotFoundError**

Cause: The `expenses.json` file does not exist.

Solution: The program handles this error and returns an empty list. The JSON file is created automatically when expenses are saved.

**2. JSONDecodeError**

Cause: The `expenses.json` file contains invalid JSON data.

Solution: Check the file contents and make sure the JSON format is correct. The current program does not handle this error automatically.

**3. ModuleNotFoundError**

Cause: The `python-dotenv` package is not installed.

Solution: Run this command in Terminal:

```bash
python -m pip install python-dotenv
```

**4. Admin Login Failed**

Cause: The entered password does not match the environment variable.

Solution: Check the `.env` file and make sure the variable name is correct:

```env
EXPENSE_TRACKER_ADMIN_PASSWORD=your_password_here
```

Also make sure `load_dotenv()` is called before checking the password.