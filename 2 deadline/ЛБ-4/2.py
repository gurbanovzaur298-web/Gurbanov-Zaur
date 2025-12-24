import random
chisla = []
for i in range(10):
    chislo = random.randint(1, 100) 
    chisla.append(chislo)
print(f"исходный список: {chisla}")
chetnye = []
for chislo in chisla:
    if chislo % 2 == 0:
        chetnye.append(chislo)
print(f"четные числа: {chetnye}")
bolshe_50 = []
for chislo in chisla:
    if chislo > 50:
        bolshe_50.append(chislo)
print(f"числа больше 50: {bolshe_50}")
print(f"\nвсего чисел: {len(chisla)}")
print(f"нашел четных: {len(chetnye)}")
print(f"нашел больше 50: {len(bolshe_50)}")