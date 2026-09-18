# Student Records

with open("students.txt", "r") as file:
    students = file.readlines()

total = 0
count = 0

print("===== STUDENT RECORDS =====")

for student in students:
    data = student.strip().split(",")

    name = data[0]
    marks = int(data[1])

    print(name, "-", marks)

    total += marks
    count += 1

average = total / count

print()
print("Total Students:", count)
print("Average Marks:", average)