numbers = [12, 45, 23, 67, 34, 89, 10]

largest = numbers[0] 

for number in numbers:
    if largest < number:
        largest = number

print("Largest is" , largest)

print("----------")

count = 0

for number in numbers:
    if number % 2 == 0:
        count += 1
print(count)

print("----------")

marks = {
    "Python": 85,
    "Java": 72,
    "SQL": 91,
    "HTML": 65
}

total = 0

for mark in marks.values():
    total += mark
print("total is " , total)

Average = total / len(marks)
print("Average is " , Average)

largest = 0

for mark in marks.values():
    if mark > largest :
        largest = mark

print("Largest is " , largest)
