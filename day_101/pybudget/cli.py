from budget_manager import Budget
from transaction import Transaction
from data_handler import load_data, save_data
from utils import format_currency, validate_float
from tabulate import tabulate

def start_cli():
    data = load_data()
    budget = Budget(data["income"])
    budget.categories = data["categories"]

    while True:
        print("\n==== PyBudget Menu ====")
        print("1. Set income")
        print("2. Add expense")
        print("3. Show summary")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            income = validate_float(input("Enter your monthly income: "))
            if income is not None:
                budget.income = income

        elif choice == "2":
            category = input("Enter expense category: ")
            amount = validate_float(input("Enter expense amount: "))
            if amount is not None:
                budget.update_category(category, amount)
                tx = Transaction(amount, category, "expense")
                data["transactions"].append(tx.to_dict())

        elif choice == "3":
            summary = budget.get_summary()
            print(f"Income: {format_currency(summary['income'])}")
            print(f"Spent: {format_currency(summary['spent'])}")
            print(f"Remaining: {format_currency(summary['remaining'])}")
            print("Breakdown:")
            print(tabulate(summary['breakdown'].items(), headers=["Category", "Amount"]))

        elif choice == "4":
            data["income"] = budget.income
            data["categories"] = budget.categories
            save_data(data)
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")