
balance = float(input("Enter opening balance: ₹"))
transactions = int(input("Enter number of transactions: "))

deposit_count = 0
successful_withdrawals = 0
rejected_withdrawals = 0

for i in range(1, transactions + 1):
    print("\nTransaction", i)
    print("1. Deposit")
    print("2. Withdraw")

    choice = input("Enter your choice (1 or 2): ")
    amount = float(input("Enter amount: ₹"))

    if amount <= 0:
        print("Invalid amount")
        continue

    if choice == "1":
        balance += amount
        deposit_count += 1
        print("Deposit Successful")

    elif choice == "2":
        if amount <= balance:
            balance -= amount
            successful_withdrawals += 1
            print("Withdrawal Successful")
        else:
            rejected_withdrawals += 1
            print("Insufficient Balance")

    else:
        print("Invalid transaction type")

print("\n--- Bank Statement ---")
print("Final Balance: ₹", balance)
print("Deposit Count:", deposit_count)
print("Successful Withdrawals:", successful_withdrawals)
print("Rejected Withdrawals:", rejected_withdrawals)

if balance < 1000:
    print("Warning: Balance below ₹1,000")
