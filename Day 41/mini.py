students = {
    "Aarav": 78,
    "Priya": 95,
    "Rahul": 88,
    "Sneha": 69
}

if not students:
    print("No student records available")
else:
    topper = max(students, key=students.get)
    average = sum(students.values()) / len(students)

    print("Topper:", topper, students[topper])
    print("Class average:", average)

    print("Above average students:")

    for name, marks in students.items():
        if marks > average:
            print(name, marks)