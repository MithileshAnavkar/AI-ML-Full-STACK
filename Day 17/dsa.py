class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def study(self):
        print(self.name, "is studying")


class CollegeStudent(Student):
    def __init__(self, name, age, college):
        super().__init__(name, age)
        self.college = college


student1 = CollegeStudent("Mithilesh", 21, "XYZ College")

print("Name:", student1.name)
print("Age:", student1.age)
print("College:", student1.college)

student1.study()