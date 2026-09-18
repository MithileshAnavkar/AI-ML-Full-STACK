name = input("Enter student name: ")
marks1 = int(input("Enter marks for Subject 1: "))
marks2 = int(input("Enter marks for Subject 2: "))
marks3 = int(input("Enter marks for Subject 3: "))
marks4 = int(input("Enter marks for Subject 4: "))
marks5 = int(input("Enter marks for Subject 5: "))
total = marks1 + marks2 + marks3 + marks4 + marks5
Percentage = total / 500 * 100
print("Student Name:", name)
print("Total Marks:", total)
print("Percentage:", Percentage, "%")