from flask import Flask, render_template, request, redirect
from manager import ExpenseManager
from validator import validate_amount
from datetime import datetime

app = Flask(__name__)
manager = ExpenseManager()


# Home page
@app.route('/')
def home():
    expenses = manager.total_with_items()
    total = manager.total_spent()
    daily = sum(exp["amount"] for exp in manager.daily_expenses())
    weekly = sum(exp["amount"] for exp in manager.weekly_expenses())
    monthly = sum(exp["amount"] for exp in manager.monthly_expenses())

    return render_template(
        'home.html',
        expenses=expenses,
        total=total,
        daily=daily,
        weekly=weekly,
        monthly=monthly
    )


# Add expense
@app.route('/add', methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST':
        name = request.form['name']
        amount = request.form['amount']
        category = request.form['category']

        try:
            amount = float(amount)
        except:
            return "❌ Amount must be a number!"

        if amount < 0:
            return "❌ Amount cannot be negative!"

        if not validate_amount(amount):
            return "❌ Invalid amount!"

        manager.add_expense(name, amount, category, date=datetime.now().date())
        return redirect('/')

    return render_template('add.html')


# Edit expense
@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit_expense(index):
    expense = manager.expenses[index]

    if request.method == 'POST':
        name = request.form['name']
        amount = float(request.form['amount'])
        category = request.form['category']

        if amount < 0:
            return "❌ Amount cannot be negative!"

        manager.update_expense(index, name, amount, category)
        return redirect('/')

    return render_template('edit.html', expense=expense, index=index)


# Delete expense
@app.route('/delete/<int:index>')
def delete_expense(index):
    manager.delete_expense(index)
    return redirect('/')


# View by category
@app.route('/category', methods=['GET', 'POST'])
def view_category():
    expenses = []
    category = None

    if request.method == 'POST':
        category = request.form['category']
        expenses = manager.view_by_category(category)

    return render_template('category.html', expenses=expenses, category=category)


if __name__ == "__main__":
    app.run(debug=True)
