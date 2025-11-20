def validate_amount(amount):
    if not isinstance(amount, (int, float)):
        print("Error: amount must be a number (int or float).")
        return False
    if amount < 0:
        print("Error: amount cannot be negative.")
        return False
    return True


def validate_date(date):
    if not (isinstance(date, tuple) and len(date) == 3):
        print("Error: date must be a tuple like (year, month, day).")
        return False

    year, month, day = date

    if not isinstance(year, int) or year < 1900:
        print("Invalid year.")
        return False
    if not isinstance(month, int) or not (1 <= month <= 12):
        print("Invalid month.")
        return False
    if not isinstance(day, int) or not (1 <= day <= 31):
        print("Invalid day.")
        return False

    return True
