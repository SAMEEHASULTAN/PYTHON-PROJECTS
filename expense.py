import csv
from datetime import datetime

FILE_NAME = "expenses.csv"

# Create CSV file if not exists
def initialize_file():
    try:
        open(FILE_NAME, "x").write("date,description,amount,category\n")
    except:
        pass

# Add expense
def add_expense():
    date = datetime.now().strftime("%Y-%m-%d")
    description = input("Description: ")
    amount = input("Amount: ")
    category = input("Category: ")

    with open(FILE_NAME, "a") as f:
        f.write(f"{date},{description},{amount},{category}\n")

    print("Expense added!\n")

# View all expenses
def view_expenses():
    print("\n--- All Expenses ---")
    with open(FILE_NAME, "r") as f:
        for line in f.readlines()[1:]:  # skip header
            print(line.strip())
    print()

# Summary by category
def summary():
    print("\n--- Summary ---")
    totals = {}

    with open(FILE_NAME, "r") as f:
        for line in f.readlines()[1:]:
            parts = line.strip().split(",")
            amount = float(parts[2])
            category = parts[3]

            if category not in totals:
                totals[category] = 0
            totals[category] += amount

    for c in totals:
        print(c, ":", totals[c])
    print()

# Main menu
def main():
    initialize_file()

    while True:
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Summary")
        print("4. Exit")

        ch = input("Choose: ")

        if ch == "1":
            add_expense()
        elif ch == "2":
            view_expenses()
        elif ch == "3":
            summary()
        elif ch == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.\n")

main()
