
students = int(input("Enter number of students: "))

total = 0
pass_count = 0
fail_count = 0

for i in range(1, students + 1):
    name = input(f"\nEnter name of student {i}: ")

    marks = float(input("Enter marks out of 100: "))

    while marks < 0 or marks > 100:
        print("Invalid marks! Enter marks between 0 and 100.")
        marks = float(input("Enter marks again: "))

    total = total + marks

    if marks >= 75:
        grade = "A"
    elif marks >= 60:
        grade = "B"
    elif marks >= 50:
        grade = "C"
    elif marks >= 40:
        grade = "D"
    else:
        grade = "Fail"

    if marks >= 40:
        pass_count += 1
    else:
        fail_count += 1

    print(name, "Grade:", grade)

average = total / students

print("\n--- Class Report ---")
print("Class Average:", average)
print("Pass Count:", pass_count)
print("Fail Count:", fail_count)
