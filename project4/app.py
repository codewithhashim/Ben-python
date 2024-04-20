expenses = {}

while True:
    print("\nExpense Tracker Menu:")
    print("1. Add Expense")
    print("2. View Summary")
    print("3. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        category = input("Enter expense category: ")
        amount = float(input("Enter expense amount: $"))
        expenses.setdefault(category, 0)
        expenses[category] += amount
        print("Expense added successfully!")
    elif choice == "2":
        print("\nExpense Summary:")
        total_spent = 0
        for category, amount in expenses.items():
            print(f"{category}: ${amount}")
            total_spent += amount
        print(f"Total Spent: ${total_spent}")
    elif choice == "3":
        print("Exiting Expense Tracker. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

print(type(expenses))