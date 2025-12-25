class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    def __add__(self, other):
        if isinstance(other, Vector):
            new_x = self.x + other.x
            new_y = self.y + other.y
            return Vector(new_x, new_y)
        else:
            return "не могу сложить"
    def __sub__(self, other):
        if isinstance(other, Vector):
            new_x = self.x - other.x
            new_y = self.y - other.y
            return Vector(new_x, new_y)
        else:
            return "не могу вычесть"
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            new_x = self.x * other
            new_y = self.y * other
            return Vector(new_x, new_y)
        elif isinstance(other, Vector):
            result = self.x * other.x + self.y * other.y
            return result
        else:
            return "не могу умножить"
    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return False
v1 = Vector(2, 3)
v2 = Vector(4, 1)
print(f"v1 = {v1}")
print(f"v2 = {v2}")
print(f"v1 + v2 = {v1 + v2}")
print(f"v1 - v2 = {v1 - v2}")
print(f"v1 * 3 = {v1 * 3}")
print(f"v1 * v2 = {v1 * v2}")
print(f"v1 == Vector(2, 3): {v1 == Vector(2, 3)}")
print(f"v1 == Vector(1, 2): {v1 == Vector(1, 2)}")
print()