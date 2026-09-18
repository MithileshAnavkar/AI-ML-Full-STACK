numbers = [-5, 10, -2, 8, 0, 15,10, 10 , -7]

count = 0

for number in numbers:
    if number > 0:
        count += 1
print("----------")
print(count)

print("----------")

min = numbers[0]

for number in numbers:
    if number < min:
        min = number
print(min)

print("----------")

count =  0

for number in numbers:
    if number == 10:
        count += 1
print("total 10 is " , count)

print("----------")

numbers = [10, 15, 20, 25, 30, 35, 40]

even = numbers[0]
total = 0

for number in numbers:
    if number % 2 == 0:
        even  = number
        total = total + even
print(total)

print("----------")

numbers = [1, 2, 3, 4, 5]

print(numbers[::-1])
