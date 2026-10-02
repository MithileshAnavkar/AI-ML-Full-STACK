def numbers(n):
    for i in range(1, n + 1):
        yield i


def even_numbers(n):
    for i in range(2, n + 1, 2):
        yield i


def squares(n):
    for i in range(1, n + 1):
        yield i ** 2


n = int(input("Enter number: "))

print("\nNumbers:")

for number in numbers(n):
    print(number)


print("\nEven Numbers:")

for number in even_numbers(n):
    print(number)


print("\nSquares:")

for square in squares(n):
    print(square)