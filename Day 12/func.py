def square(number):
    print(square(5))
print("----------")
def calculate_sum(numbers):
    total = 0

    for number in numbers:
        total += number

    return total


marks = [80, 75, 90, 65]

print(calculate_sum(marks))
print("----------")

def find_largest(numbers):
    largest = numbers[0]

    for number in numbers:
        if number >  largest:
            largest = number

    return largest
numbers = [10, 45, 23, 67, 12]
print(find_largest(numbers))
print("----------")
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    print("Result:", add(num1, num2))

elif operator == "-":
    print("Result:", subtract(num1, num2))

elif operator == "*":
    print("Result:", multiply(num1, num2))

elif operator == "/":
    if num2 == 0:
        print("Cannot divide by zero")
    else:
        print("Result:", divide(num1, num2))

else:
    print("Invalid operator")