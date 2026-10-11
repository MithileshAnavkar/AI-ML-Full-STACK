def greater_than_ten(numbers):
    for number in numbers:
        if number > 10:
            yield number

data = [5, 12, 8, 20, 15, 3]

for number in greater_than_ten(data):
    print(number)