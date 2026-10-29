
days = int(input("Enter number of days: "))

total_units = 0
high_usage_days = 0
maximum_usage = 0

for i in range(1, days + 1):
    units = float(input(f"Enter units used on day {i}: "))

    total_units += units

    if units > 10:
        high_usage_days += 1

    if units > maximum_usage:
        maximum_usage = units

average = total_units / days

print("\n--- Electricity Report ---")
print("Total Units:", total_units)
print("Average Usage:", average)
print("Days Above 10 Units:", high_usage_days)
print("Maximum Daily Usage:", maximum_usage)

if total_units > 300:
    print("High Usage")
else:
    print("Normal Usage")
