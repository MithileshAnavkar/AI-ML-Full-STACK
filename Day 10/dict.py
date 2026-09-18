student = {
    "name": "Mithilesh",
    "age": "20",
    "Branch": "Comps"
}
print(student["name"])
print(student["age"])
print(student["Branch"])
print("----------")
student["college"] = "SCOE"
student["age"] = "22"
student.pop("Branch")
print(student)
print("----------")
for key in student:
    print(key)
print("----------")
for values in student.values():
    print(values)
print("----------")
for key,values in student.items():
    print(key ,":", values)
print("----------")

