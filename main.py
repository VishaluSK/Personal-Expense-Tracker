from manager import ExpenseManager

def show_menu():
    print("\n=== Personal Expense Tracker ===")
    print("1. Add Expense")
    print("2. View by Category")
    print("3. View Total Spent")
    print("4. Exit")

def main():
    manager = ExpenseManager()

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            category = input("Enter category: ")
            amount = float(input("Enter amount: "))
            note = input("Optional note: ")

            manager.add_expense(category, amount, note)
            print("Expense added successfully!")

        elif choice == "2":
            category = input("Enter category name: ")
            results = manager.view_by_category(category)

            if not results:
                print("No expenses found for this category.")
            else:
                print(f"\nExpenses under '{category}':")
                for exp in results:
                    print(f"- ₹{exp.amount} | {exp.note}")

        elif choice == "3":
            total = manager.total_spent()
            print(f"\nTotal Spent: ₹{total}")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    