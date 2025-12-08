print("Введите три целых числа через пробел:")
a, b, c = map(int, input().split())

mult1 = a * b
mult2 = b * c  
mult3 = c * a

power4 = a ** 4
remainder = b % c
division = c // a

print("\nРезультаты умножения:")
print(f"a * b = {mult1}")
print(f"b * c = {mult2}")
print(f"c * a = {mult3}")

print("\nРезультаты дополнительных операций:")
print(f"a в 4 степени = {power4}")
print(f"остаток от деления b на c = {remainder}")
print(f"целочисленное деление c на a = {division}")

print("\nСумма переменных из пункта 5:")
sum_result = power4 + remainder + division

print(f"{power4} + {remainder} + {division} = {sum_result}")
