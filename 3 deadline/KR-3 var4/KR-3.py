class Box:
    def __init__(self, volume):
        if volume < 0:
            print("внимание: объем не может быть отрицательным! установлено 0")
            self.volume = 0
        else:
            self.volume = volume
    def __str__(self):
        return f"коробка объемом: {self.volume}"
    def __add__(self, other):
        if isinstance(other, Box):
            new_volume = self.volume + other.volume
            return Box(new_volume)
        else:
            return "не могу сложить с этим объектом"
    def __mul__(self, n):
        if isinstance(n, (int, float)):
            new_volume = self.volume * n
            return Box(new_volume)
        else:
            return "не могу умножить на это значение"
    def __eq__(self, other):
        if isinstance(other, Box):
            return self.volume == other.volume
        return False
print("=== демонстрация работы класса box ===")
print()
box1 = Box(10)
box2 = Box(20)
box3 = Box(10)
print(f"   box1: {box1}")
print(f"   box2: {box2}")
print(f"   box3: {box3}")
print()
box_sum = box1 + box2
print(f"   box1 + box2 = {box_sum}")
print(f"   тип результата: {type(box_sum)}")
print()
box_mult1 = box1 * 3
box_mult2 = box2 * 1.5

print(f"   box1 * 3 = {box_mult1}")
print(f"   box2 * 1.5 = {box_mult2}")
print()
print(f"   box1 == box2: {box1 == box2}")
print(f"   box1 == box3: {box1 == box3}")
print(f"   box1 == Box(10): {box1 == Box(10)}")
print()
box_chain = box1 + box2 * 2
print(f"   box1 + box2 * 2 = {box_chain}")
box_negative = Box(-5)
print(f"   коробка с отрицательным объемом: {box_negative}")
print()
print("6. использование print:")
print(f"   просто print(box1): {box1}")
print(f"   просто print(box2): {box2}")
print("\n7. проверка создания новых объектов:")
print(f"   исходный box1: {box1}")
print(f"   после операций box1 остался тем же: {box1}")