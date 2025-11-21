Perfect! Here’s a **short, GitHub-ready, beginner-friendly README** version with badges and emojis that you can directly add to your rep
Personal Expense Tracker

A simple and beginner-friendly Expense Tracker** built with Python.
Record, manage, and analyze your daily expenses with ease — either via command-line or web interface (Flask)

Features
* Add new expenses (name, amount, category)
* View all expenses in a clean table
* Edit or delete any expense
* Saves all data in a JSON file
* View expenses by category (supports partial matches)
* Daily / Weekly / Monthly total spending
* Error handling for invalid or negative inputs
* Beginner-friendly and easy to extend

Tech Stack

* Python 3
* JSON (persistent storage)
* Flask (optional web interface)
* tabulate (optional CLI table formatting)

Installation & Usage

1. Clone the repo:

git clone https://github.com/VishaluSK/Personal-Expense-Tracker.git
cd personal_expense_tracker

2. Install dependencies:
pip install flask tabulate

3. Run the CLI version
python main.py

4. Run the Web version (optional)
python app.py

Open browser at [http://127.0.0.1:5000/](http://127.0.0.1:5000/)


Folder Structure

```
personal_expense_tracker/
├─ main.py
├─ manager.py
├─ validator.py
├─ mode.py
├─ paths.py
├─ utils.py
├─ app.py
├─ templates/
└─ data/expenses.json


