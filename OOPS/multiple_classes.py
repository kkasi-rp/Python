class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_students(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_avg_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)

s1 = Student('KK', 35, 95)
s2 = Student('Pushpa', 28, 81)
s3 = Student('Purvi', 8, 98)

course = Course("Computers", 2)
course.add_students(s1)
course.add_students(s2)
print(course.add_students(s3))
print(course.students)
print(course.students[0].name)
print(course.get_avg_grade())