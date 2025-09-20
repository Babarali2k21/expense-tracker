from src.tracker.expense import add_expense, get_expenses, delete_expense


def main():
    print("Expense Tracker CLI")
    while True:
        print("\nOptions:")
        print("1. Add expense")
        print("2. View expenses")
        print("3. Delete expense")
        print("4. Exit")

        choice = input("Choose (1/2/3/4): ").strip()

        if choice == "1":
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            description = input("Enter description: ")
            expense = add_expense(amount, category, description)
            print(f"Added: {expense}")

        elif choice == "2":
            expenses = get_expenses()
            if not expenses:
                print("No expenses recorded yet.")
            else:
                print("\nYour Expenses:")
                for e in expenses:
                    print(f"ID {e['id']}: {e['amount']} - {e['category']} ({e['description']})")

        elif choice == "3":
            expenses = get_expenses()
            if not expenses:
                print("No expenses to delete.")
            else:
                print("\nYour Expenses:")
                for e in expenses:
                    print(f"ID {e['id']}: {e['amount']} - {e['category']} ({e['description']})")

                try:
                    expense_id = int(input("Enter the expense ID to delete: "))
                    removed = delete_expense(expense_id)
                    if removed:
                        print(f"Deleted: {removed}")
                    else:
                        print("Invalid expense ID.")
                except ValueError:
                    print("Please enter a valid number.")

        elif choice == "4":
            break

        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()