
number = int(input("Enter a positive integer: "))

while number <= 0:
    print("Please enter a positive integer.")
    number = int(input("Enter a positive integer: "))

print("\n--- Multiplication Table ---")

for i in range(1, 11):
    print(number, "x", i, "=", number * i)

start = int(input("\nEnter starting number: "))
end = int(input("Enter ending number: "))

while start > end:
    print("Start must not be greater than end.")
    start = int(input("Enter starting number again: "))
    end = int(input("Enter ending number again: "))

even_count = 0
odd_count = 0
total = 0

for i in range(start, end + 1):
    total += i

    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("\n--- Number Analysis ---")
print("Even Count:", even_count)
print("Odd Count:", odd_count)
print("Sum of Range:", total)
