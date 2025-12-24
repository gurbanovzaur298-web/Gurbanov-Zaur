import random
zagadannoe = random.randint(1, 100)
print("я загадал число от 1 до 100. попробуй угадать!")
popytki = 0
while True:
    vvod = input("твоя догадка: ")
    if vvod.isdigit():
        popytka = int(vvod)
        popytki += 1
        if popytka < zagadannoe:
            print("мое число больше")
        elif popytka > zagadannoe:
            print("мое число меньше")
        else:
            print(f"ура! ты угадал с {popytki} попытки!")
            break
    else:
        print("введи число, а не буквы!")
print(f"было загадано число {zagadannoe}")