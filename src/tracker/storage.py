import json
import os
from typing import List, Dict

DATA_FILE = "data/expenses.json"

def load_expenses() -> List[Dict]:
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_expenses(expenses: List[Dict]) -> None:
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=2)