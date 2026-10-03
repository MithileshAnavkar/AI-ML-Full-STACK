from dataclasses import dataclass

@dataclass
class Student:
    name: str
    marks: float
    branch: str


students = []

# Add students
students.append(Student("Mithilesh", 91, "Computer"))
students.append(Student("Rahul", 84, "Computer"))
students.append(Student("Amit", 78, "IT"))

# Display
for student in students:
    print(student)

# Topper
topper = max(students, key=lambda s: s.marks)

print("\nTopper:", topper.name)
print("Marks:", topper.marks)

# Average
average = sum(s.marks for s in students) / len(students)

print("Average:", average)