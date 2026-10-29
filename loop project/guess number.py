
secret_number = 37
attempts = 0
max_attempts = 5
won = False

while attempts < max_attempts:
    guess = int(input("Guess the secret number: "))
    attempts += 1

    if guess == secret_number:
        print("Congratulations! You guessed correctly.")
        won = True
        break
    elif guess < secret_number:
        print("Too low")
    else:
        print("Too high")

if won:
    print("You Win!")
else:
    print("You Lose!")
    print("The secret number was:", secret_number)

print("Attempts Used:", attempts)
