ocenki = []
ocenki.append(5)
ocenki.append(4)
ocenki.append(3)
ocenki.append(5)
ocenki.append(2)
print(f"текущие оценки: {ocenki}")
udaleno_pervaya = ocenki.pop(0)
print(f"удалил первую оценку: {udaleno_pervaya}")
udaleno_poslednyaya = ocenki.pop(-1)
print(f"удалил последнюю оценку: {udaleno_poslednyaya}")
summa_ocenok = 0
for ocenka in ocenki:
    summa_ocenok += ocenka
sredniy_ball = summa_ocenok / len(ocenki)
print(f"средний балл: {sredniy_ball}")
print(f"итоговые оценки: {ocenki}")