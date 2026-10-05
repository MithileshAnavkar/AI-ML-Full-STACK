from collections import defaultdict

students = [
    ("Mithilesh", "Computer"),
    ("Rahul", "IT"),
    ("Amit", "Computer"),
    ("Neha", "IT"),
    ("Priya", "Electronics"),
    ("Rohan", "Computer")
]

departments = defaultdict(list)

for name, department in students:
    departments[department].append(name)

for department, students_list in departments.items():
    print(f"\n{department}:")

    for student in students_list:
        print(student)