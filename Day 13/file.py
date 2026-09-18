file = open("dict.txt", "r")
data = file.read()
print(data)
file.close()
print("----------")
with open("dict.txt", "r") as file:
    line = file.readline()
    print(line)