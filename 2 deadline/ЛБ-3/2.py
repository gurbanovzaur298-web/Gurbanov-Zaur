text = input("Введите произвольный текст: ")

text = text.lower()

char_count = {}

for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print("Результат подсчета символов:")
print(char_count)