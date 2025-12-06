count = 0

print("Вводите числа (для завершения введите 0):")

while True:
    try:
        num = float(input())
        
        if num == 0:
            break
        else:
            count += 1
    except ValueError:
        print("Пожалуйста, введите число!")

print(f"Количество введенных чисел: {count}")