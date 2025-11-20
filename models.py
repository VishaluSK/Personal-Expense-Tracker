from dataclasses import dataclass, asdict

@dataclass
class Expense:
    name: str
    amount: float
    category: str
    date: tuple  # (year, month, day)

    def to_dict(self):
        d = asdict(self)
        d["date"] = list(self.date)  # convert tuple → list for JSON
        return d

    @staticmethod
    def from_dict(d):
        return Expense(
            name=d["name"],
            amount=d["amount"],
            category=d["category"],
            date=tuple(d["date"])  # convert list → tuple
        )
