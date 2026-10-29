
questions = [
    ("What is the capital of India? ", "delhi"),
    ("How many days are there in a week? ", "7"),
    ("What is 5 + 5? ", "10"),
    ("Which language are we learning? ", "python"),
    ("How many months are there in a year? ", "12")
]

score = 0

for question, answer in questions:
    user_answer = input(question).strip().lower()

    if user_answer == answer:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

total_questions = len(questions)
percentage = (score / total_questions) * 100

print("\n--- Quiz Result ---")
print("Score:", score, "/", total_questions)
print("Percentage:", percentage, "%")

if percentage >= 80:
    print("Excellent")
elif percentage >= 60:
    print("Good")
else:
    print("Keep Practicing")
