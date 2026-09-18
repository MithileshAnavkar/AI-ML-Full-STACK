fruits = {"apple","mango","banana"}
fruits.add("grapes")
fruits.remove("mango")
print(fruits)
print("----------")
print("apple" in fruits)
print("----------")
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A | B)
print(A & B)
print(A - B)
print("----------")

numbers = [10, 20, 20, 30, 40, 40, 50]

unique_number = set(numbers)
print(unique_number)
print("----------")

numbers = {1, 2, 3, 5}

full_number = set(range(1,6))
missing = full_number - numbers
print(missing)