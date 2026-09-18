marks = {
    "Python": 85,
    "Java": 72,
    "SQL": 91,
    "HTML": 65,
    "CSS": 78
}

total = 0
highest = 0
lowest = marks["Python"]
top_subject = ""

passed = 0
failed = 0

for subject, mark in marks.items():

    # Calculate total
    total += mark

    # Find highest marks
    if mark > highest:
        highest = mark
        top_subject = subject

    # Find lowest marks
    if mark < lowest:
        lowest = mark

    # Count passed and failed subjects
    if mark >= 40:
        passed += 1
    else:
        failed += 1

# Calculate average
average = total / len(marks)

print("===== STUDENT MARKS ANALYZER =====")

print("Total Marks:", total)
print("Average Marks:", average)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Passed Subjects:", passed)
print("Failed Subjects:", failed)
print("Top Subject:", top_subject)