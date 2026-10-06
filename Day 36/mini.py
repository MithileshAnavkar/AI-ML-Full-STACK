from functools import reduce
result = reduce(lambda a, b: a * b,range(1,7))
print(result)