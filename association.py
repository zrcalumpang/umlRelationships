class Student:
    def __init__(self, name):
        self.name = name


class Teacher:
    def teach(self, student):
        print(f"Teaching {student.name}")


student = Student("Zoe")
teacher = Teacher()

teacher.teach(student)
