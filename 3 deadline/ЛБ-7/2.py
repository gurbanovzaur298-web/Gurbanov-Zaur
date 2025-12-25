class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary
    @property
    def salary(self):
        return self._salary
    @salary.setter
    def salary(self, value):
        if value < 0:
            print("ошибка: зарплата не может быть отрицательной!")
            return
        self._salary = value
emp = Employee("Арсюша", 50000)
print(f"сотрудник: {emp.name}, зарплата: {emp.salary}")
print("\nпробуем поставить отрицательную зарплату:")
emp.salary = -100  
print(f"зарплата после попытки: {emp.salary}")  
print("\nпробуем поставить нормальную зарплату:")
emp.salary = 60000 
print(f"зарплата после изменения: {emp.salary}")
print()