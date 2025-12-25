class StringUtils:
    @staticmethod
    def invert(string):
        return string[::-1]    
    @staticmethod
    def normalize(string):
        return string.strip().lower()
class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role
    @classmethod
    def from_string(cls, data_string):
        parts = data_string.split(';')
        if len(parts) == 2:
            name, role = parts
            return cls(name, role)
        else:
            return cls("неизвестно", "гость")
print("работа со строками:")
print(f"invert('Hello'): {StringUtils.invert('Hello')}")
print(f"normalize('  DATA  '): {StringUtils.normalize('  DATA  ')}")
print("\nработа с пользователями:")
user1 = User.from_string("Мага;Admin")
print(f"user1: имя={user1.name}, роль={user1.role}")
user2 = User.from_string("Амир;User")
print(f"user2: имя={user2.name}, роль={user2.role}")
user3 = User.from_string("ТолькоИмя")  
print(f"user3: имя={user3.name}, роль={user3.role}")
print()