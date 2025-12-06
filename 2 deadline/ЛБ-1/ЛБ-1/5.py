text = input("Введите строку: ")

vowels = 'аеёиоуыэюяaeiou'
vowels += vowels.upper()  # добавляем заглавные буквы

result = ""
index = 0

while index < len(text):
    char = text[index]
    if char not in vowels:
        result += char
    index += 1

print(f"Результат: {result}")