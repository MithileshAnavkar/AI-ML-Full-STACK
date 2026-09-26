import json

json_data = '{"name": "Mithilesh", "age": 21, "course": "BE Computer Engineering"}'

student = json.loads(json_data)
print(student)
print(student["name"])
print(student["age"])