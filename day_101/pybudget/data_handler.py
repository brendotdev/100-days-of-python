import json

DATA_FILE = "data/budget.json"

def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"income": 0, "categories": {}, "transactions": []}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


# pybudget/utils.py
def format_currency(amount):
    return f"${amount:.2f}"


def validate_float(input_str):
    try:
        return float(input_str)
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None