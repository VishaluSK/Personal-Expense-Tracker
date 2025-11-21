from datetime import datetime, timedelta

class ExpenseManager:
    def __init__(self):
        self.expenses = []   # list of dictionaries

    def add_expense(self, name, amount, category, date=None):
        if date is None:
            date = datetime.now().date()

        self.expenses.append({
            "name": name,
            "amount": float(amount),
            "category": category,
            "date": date
        })

    def view_by_category(self, category):
        category = category.strip().lower()
        return [exp for exp in self.expenses if category in exp["category"].strip().lower()]

    def total_spent(self):
        return sum(exp["amount"] for exp in self.expenses)

    def total_with_items(self):
        return self.expenses

    def daily_expenses(self):
        today = datetime.now().date()
        return [exp for exp in self.expenses if exp["date"] == today]

    def weekly_expenses(self):
        today = datetime.now().date()
        week_ago = today - timedelta(days=7)
        return [exp for exp in self.expenses if week_ago <= exp["date"] <= today]

    def monthly_expenses(self):
        today = datetime.now().date()
        return [exp for exp in self.expenses if exp["date"].month == today.month and exp["date"].year == today.year]

    # New method: delete expense by index
    def delete_expense(self, index):
        if 0 <= index < len(self.expenses):
            self.expenses.pop(index)

    # New method: update expense by index
    def update_expense(self, index, name, amount, category):
        if 0 <= index < len(self.expenses):
            self.expenses[index]["name"] = name
            self.expenses[index]["amount"] = float(amount)
            self.expenses[index]["category"] = category
