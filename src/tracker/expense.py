import json
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parents[2] / "data" / "expenses.json"


def _load_data():
    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []


def _save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


def add_expense(amount: float, category: str, description: str = ""):
    """Add a new expense with unique ID."""
    data = _load_data()
    new_id = 1 if not data else max(e["id"] for e in data) + 1
    expense = {
        "id": new_id,
        "amount": amount,
        "category": category,
        "description": description,
    }
    data.append(expense)
    _save_data(data)
    return expense


def get_expenses():
    """Retrieve all expenses."""
    return _load_data()


def delete_expense(expense_id: int):
    """Delete expense by its unique ID."""
    data = _load_data()
    for i, e in enumerate(data):
        if e["id"] == expense_id:
            removed = data.pop(i)
            _save_data(data)
            return removed
    return None
