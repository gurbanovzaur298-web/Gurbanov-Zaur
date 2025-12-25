class Student:
    def __init__(self, name, average_score):
        self.name = name
        self.average_score = average_score
    def is_excellent(self):
        if self.average_score == 5:
            return True
        else:
            return False
student1 = Student("Вася", 4.5)
student2 = Student("Петя", 5)
print(f"{student1.name}: отличник? {student1.is_excellent()}")
print(f"{student2.name}: отличник? {student2.is_excellent()}")
student3 = Student("Маша", 4.8)
print(f"{student3.name}: отличник? {student3.is_excellent()}")