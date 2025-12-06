fruits = {
    'яблоки': 5,
    'бананы': 3,
    'апельсины': 10,
    'арбузы': 33
}

print("Начальный запас фруктов:")
for fruit, count in fruits.items():
    print(f"За прилавком есть {count} {fruit}")

print("\n" + "="*40)

fruits['яблоки'] -= 2
print("Продали 2 яблока")

fruits['арбузы'] = 0
print("Мага Похититель Арбузов украл все арбузы!")

print("\n" + "="*40)

print("Итоговый запас фруктов:")
for fruit, count in fruits.items():
    print(f"За прилавком осталось {count} {fruit}")