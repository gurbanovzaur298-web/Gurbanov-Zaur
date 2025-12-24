print("сумма цифр числа")

chislo = input("введи положительное целое число: ")

if chislo.isdigit():
    chislo_int = int(chislo)
    
    rabochee_chislo = chislo_int
    
    summa = 0
    while rabochee_chislo > 0:
        poslednyaya_cifra = rabochee_chislo % 10
        summa = summa + poslednyaya_cifra
        rabochee_chislo = rabochee_chislo // 10
        print(f"взял цифру {poslednyaya_cifra}, сумма сейчас {summa}")
    print(f"сумма всех цифр числа {chislo_int} = {summa}")
else:
    print("это не число!")