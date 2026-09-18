numbers = [4, 7, 2, 4, 9, 7, 5, 2, 1]

seen = set()
duplicates = set()
for num in numbers:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)

print(duplicates)
