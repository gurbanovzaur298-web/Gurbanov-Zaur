num = int(input("Введите положительное целое число: "))

if num <= 0:
    print("Ошибка: число должно быть положительным!")
else:
    digit_sum = 0
    
    while num > 0:
        digit = num % 10
        digit_sum += digit
        num //= 10
    
    print(f"Сумма цифр: {digit_sum}")