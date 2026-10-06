from typing import TypedDict

class Student(TypedDict):
    id: int
    name: str
    skills: list[str]
    cgpa: float


student: Student = {
    "id": 101,
    "name": "Mithilesh",
    "skills": ["Python", "React", "SQL"],
    "cgpa": 8.67
}

print(student["name"])
print(student["skills"])