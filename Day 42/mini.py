task = input("Enter a completed task: ")

with open("tasks.txt", "a") as file:
    file.write(task + "\n")

print("\nYour saved tasks:")

with open("tasks.txt", "r") as file:
    for line in file:
        print(line.strip())