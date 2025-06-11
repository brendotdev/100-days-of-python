# PyBudget

A personal budgeting and expense tracker built with Python. This command-line application allows users to input, categorize, and analyze expenses while setting a monthly budget cap. It’s designed to help users stay financially disciplined and make informed money decisions.

---

## Features

* Add, edit, or delete expenses
* Set a monthly budget
* Categorize expenses (e.g., Food, Rent, Entertainment)
* View spending breakdown by category
* Visualize budget usage with a progress bar
* Persist data locally using JSON

---

## Usage

### Run the Application

```bash
python pybudget.py
```

### Menu Options

1. Add new expense
2. View all expenses
3. Edit or delete an expense
4. Set monthly budget
5. View budget usage
6. Exit

---

## Sample Output

```
==== PyBudget ====
1. Add Expense
2. View Expenses
3. Edit/Delete Expense
4. Set Budget
5. View Budget Usage
6. Exit
Enter your choice:
```

---

## File Structure

```
pybudget/
├── pybudget.py
├── budget_data.json
├── README.md
```

---

## Technologies Used

* Python 3.x
* `json` for persistent storage
* ANSI escape codes for terminal colors and progress visualization

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/pybudget.git
cd pybudget
```

Make sure you have Python 3 installed:

```bash
python3 --version
```

Run the script:

```bash
python pybudget.py
```

---

## Git Commands

```bash
git add pybudget.py README.md budget_data.json
git commit -m "feat: add PyBudget CLI app with budget tracking and JSON persistence"
```

---

## License

MIT License
