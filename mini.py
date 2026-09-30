def number_generator(n):

    for i in range(1, n + 1):
        yield i


def square_generator(n):

    for i in range(1, n + 1):
        yield i * i


n = int(input("Enter number: "))

print("\nNumbers:")

for number in number_generator(n):
    print(number)

print("\nSquares:")

for square in square_generator(n):
    print(square)