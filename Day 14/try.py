def calculator(a, b, operator):
    try:
        if operator == "+":
            return a + b

        elif operator == "-":
            return a - b

        elif operator == "*":
            return a * b

        elif operator == "/":
            return a / b

        else:
            return "Invalid operator"

    except ZeroDivisionError:
        return "Cannot divide by zero"


print(calculator(10, 5, "+"))
print(calculator(10, 5, "*"))
print(calculator(10, 0, "/"))