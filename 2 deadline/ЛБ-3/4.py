products = {
    "ноутбук": {"price": 50000, "sold": 15},
    "мышь": {"price": 1000, "sold": 45},
    "клавиатура": {"price": 2500, "sold": 30},
    "монитор": {"price": 30000, "sold": 8}
}
print("исходные данные:")
for tovar, info in products.items():
    print(f"{tovar}: цена {info['price']} руб, продано {info['sold']} шт")
max_sold = 0
tovar_max_sold = ""
for tovar, info in products.items():
    if info["sold"] > max_sold:
        max_sold = info["sold"]
        tovar_max_sold = tovar
print(f"\n1. самый продаваемый товар: {tovar_max_sold} (продано {max_sold} шт)")
obshaya_viruchka = 0
for tovar, info in products.items():
    viruchka_tovara = info["price"] * info["sold"]
    obshaya_viruchka = obshaya_viruchka + viruchka_tovara
    print(f"{tovar}: {info['price']} * {info['sold']} = {viruchka_tovara} руб")
print(f"2. общая выручка магазина: {obshaya_viruchka} руб")
max_viruchka = 0
tovar_max_viruchka = ""
for tovar, info in products.items():
    viruchka_tovara = info["price"] * info["sold"]
    if viruchka_tovara > max_viruchka:
        max_viruchka = viruchka_tovara
        tovar_max_viruchka = tovar
print(f"3. товар с наибольшей выручкой: {tovar_max_viruchka} ({max_viruchka} руб)")