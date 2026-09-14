numbers = [5, 3, 8, 3, 9, 5, 1, 8, 6]
target = 11

# 1. Unique numbers
unique_numbers = set(numbers)
print("Unique numbers:", unique_numbers)

# 2. Duplicate numbers
seen = set()
duplicates = set()

for num in numbers:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)

print("Duplicate numbers:", duplicates)

# 3. Number of unique numbers
print("Number of unique numbers:", len(unique_numbers))

# 4. Number of duplicate values
print("Number of duplicate values:", len(duplicates))

# 5. Two Sum
seen = set()

for num in numbers:
    needed = target - num

    if needed in seen:
        print("Two numbers with sum", target, ":", needed, num)
        break

    seen.add(num)