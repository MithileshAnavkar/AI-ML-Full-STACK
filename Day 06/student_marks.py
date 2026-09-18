marks = [78, 35, 92, 67, 28, 88]

print("Student Marks Manager")
print("---------------------")
print("Marks:", marks)

total = sum(marks)
highest = max(marks)
lowest = min(marks)
average = total / len(marks)

print("Total:", total)
print("Highest:", highest)
print("Lowest:", lowest)
print("Average:", average)

print("\nResults:")

for mark in marks:
    if mark >= 90:
        grade = "A+"
    elif mark >= 80:
        grade = "A"
    elif mark >= 70:
        grade = "B"
    elif mark >= 60:
        grade = "C"
    elif mark >= 40:
        grade = "D"
    else:
        grade = "F"

    if mark >= 40:
        status = "Pass"
    else:
        status = "Fail"

    print(mark, "-", grade, "-", status)