import json
from pathlib import Path
from collections import defaultdict

DATA_FILE = Path(__file__).resolve().parents[2] / "data" / "expenses.json"

def category_report():
    """Return total amount spent per category as a dictionary."""
    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as f:
            expenses = json.load(f)
    else:
        expenses = []

    totals = defaultdict(float)
    for e in expenses:
        totals[e["category"]] += e["amount"]

    return dict(totals)