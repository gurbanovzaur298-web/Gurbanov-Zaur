def power(a, n):
    if n == 0:
        return 1
    return a * power(a, n - 1)
print("2^3 =", power(2, 3))  
print("5^0 =", power(5, 0))  
