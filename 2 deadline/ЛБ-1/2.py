print("вводи числа, 0 - остановка")

schetchik = 0

while True:
    vvod = input("введи число (0 чтобы остановить): ")
    
    if vvod.lstrip('-').isdigit():  # разрешаю минус в начале
        chislo = int(vvod)
        if chislo == 0:
            break 
        schetchik += 1
        print(f"число {chislo} принято. всего чисел: {schetchik}")
    else:
        print("это не число, попробуй еще")
print(f"всего ввели {schetchik} чисел до нуля")