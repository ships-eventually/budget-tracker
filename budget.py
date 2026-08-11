"""Import a bank CSV export and show spend per category."""
import csv, sys
from collections import defaultdict

CATEGORIES = {"WOOLWORTHS": "groceries", "UBER": "transport", "NETFLIX": "subscriptions"}

def main(path):
    totals = defaultdict(float)
    with open(path, newline="") as f:          # BUG: exports start with a UTF-8 BOM
        for row in csv.DictReader(f):
            desc = row["Description"].upper()
            cat = next((c for k, c in CATEGORIES.items() if k in desc), "other")
            totals[cat] += float(row["Amount"])
    for cat, amt in sorted(totals.items()):
        print(f"{cat:15} R{amt:>10.2f}")

if __name__ == "__main__":
    main(sys.argv[1])
