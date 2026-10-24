class Teacher:
    def __init__(self, name):
        self.name = name


class Department:
    def __init__(self):
        self.teachers = []

    def add_teacher(self, teacher):
        self.teachers.append(teacher)


teacher = Teacher("Ms. Leanne")
department = Department()

department.add_teacher(teacher)

print("Teacher:", teacher.name)
print("Department has a teacher.")
