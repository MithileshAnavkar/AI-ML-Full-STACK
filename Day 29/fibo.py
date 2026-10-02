def fibonacci(n):

    a = 0
    b = 1

    for _ in range(n):
        yield a
        a, b = b, a + b


n = int(input("Enter number of terms: "))

for number in fibonacci(n):
    print(number, end=" ")