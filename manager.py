import os
from typing import List
from dataclasses import dataclass, asdict

from utils import load_json, save_json
from paths import DATA_FILE


@dataclass
class Expense:
    category: str
    amount: float
    note: str = ""


class ExpenseManager:
    def __init__(self, data_file=DATA_FILE):
        self.data_file = data_file
        self.categories = set()
        self.expenses: List[Expense] = []
        self._ensure_data_dir()
        self.load_expenses()

    def _ensure_data_dir(self):
        """Ensure the data directory exists"""
        os.makedirs(os.path.dirname(self.data_file), exist_ok=True)

    def load_expenses(self):
        """Load expenses from JSON file"""
        data = load_json(self.data_file)
        for item in data:
            exp = Expense(
                category=item["category"],
                amount=item["amount"],
                note=item.get("note", "")
            )
            self.expenses.append(exp)
            self.categories.add(exp.category)

    def save_expenses(self):
        """Save expenses to JSON file"""
        data = [asdict(exp) for exp in self.expenses]
        save_json(self.data_file, data)

    def add_expense(self, category, amount, note=""):
        exp = Expense(category, amount, note)
        self.expenses.append(exp)
        self.categories.add(category)
        self.save_expenses()

    def view_by_category(self, category):
        return [exp for exp in self.expenses if exp.category == category]

    def total_spent(self):
        return sum(exp.amount for exp in self.expenses)
