from functools import reduce

numbers = [2, 3, 4, 5]

total = reduce(lambda a, b: a + b, numbers)
product = reduce(lambda a, b: a * b, numbers)

print("Sum:", total)
print("Product:", product)