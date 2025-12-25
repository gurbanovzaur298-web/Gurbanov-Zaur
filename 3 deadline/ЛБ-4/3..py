class Character:
    def __init__(self, name):
        self.name = name    
    def move(self):
        print(f"{self.name} двигается")
class Archer(Character): 
    def __init__(self, name):
        super().__init__(name)     
    def shoot(self):
        print(f"{self.name} стреляет из лука")
class Knight(Character): 
    def __init__(self, name):
        super().__init__(name)
    def attack_sword(self):
        print(f"{self.name} атакует мечом")
archer = Archer("Леголас")
knight = Knight("Арагорн")
archer.move()
knight.move()
archer.shoot()
knight.attack_sword()
print(f"\nИмя лучника: {archer.name}")
print(f"Имя рыцаря: {knight.name}")