import time
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
def tail_fibonacci(n, current=0, next_num=1):
    if n == 0:
        return current
    return tail_fibonacci(n - 1, next_num, current + next_num)
n = 35
print("Обычная рекурсия:")
start_time = time.time()
result1 = fibonacci(n)
time1 = time.time() - start_time
print(f"Fibonacci({n}) = {result1}")
print(f"Время выполнения: {time1:.6f} секунд")
print("\nХвостовая рекурсия:")
start_time = time.time()
result2 = tail_fibonacci(n)
time2 = time.time() - start_time
print(f"Tail Fibonacci({n}) = {result2}")
print(f"Время выполнения: {time2:.6f} секунд")
print(f"\nРазница: обычная в {time1/time2:.0f} раз медленнее!")
print("\nПроверка для маленьких n:")
for i in range(10):
    fib1 = fibonacci(i)
    fib2 = tail_fibonacci(i)
