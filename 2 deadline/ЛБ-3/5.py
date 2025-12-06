word_stats = {}

print("Введите текст (пустая строка для завершения):")

while True:
    line = input()
    if line == "":
        break
    
    clean_line = ""
    for char in line:
        if char.isalnum() or char == " ":
            clean_line += char.lower()
        else:
            clean_line += " "

    words = clean_line.split()
    
    for word in words:
        word_stats[word] = word_stats.get(word, 0) + 1

print(f"Статистика слов: {word_stats}")