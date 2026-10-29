
days = int(input("Enter number of days: "))

total = 0
highest = 0

for i in range(1, days + 1):
    expense = float(input(f"Enter expense for day {i}: ₹"))

    total = total + expense

    if expense > highest:
        highest = expense

average = total / days

print("\n--- Expense Report ---")
print("Total Expense: ₹", total)
print("Average Daily Expense: ₹", average)
print("Highest Daily Expense: ₹", highest)

if total > 5000:
    print("Budget Alert")
else:
    print("Budget is within limit")
