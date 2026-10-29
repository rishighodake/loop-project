
correct_pin = "1234"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    pin = input("Enter your ATM PIN: ")
    attempts += 1

    if pin == correct_pin:
        print("Access Granted")
        break
    else:
        print("Incorrect PIN")

if attempts == max_attempts and pin != correct_pin:
    print("Card Temporarily Locked")

print("Attempts Used:", attempts)
