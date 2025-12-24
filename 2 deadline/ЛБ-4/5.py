text_lines = []
while True:
    line = input()
    if line == "":
        break
    text_lines.append(line)
text = " ".join(text_lines)
print(f"\nвведенный текст: {text}")
for znak in ".,!?;:()\"'-":
    text = text.replace(znak, " ")
slova = text.lower().split()
print(f"список слов (в нижнем регистре): {slova}")
if len(slova) == 0:
    print("текст не содержит слов!")
else:
    samoe_dlinnoye = slova[0]
    samoe_korotkoye = slova[0]  
    for slovo in slova:
        if len(slovo) > len(samoe_dlinnoye):
            samoe_dlinnoye = slovo
        if len(slovo) < len(samoe_korotkoye):
            samoe_korotkoye = slovo
    print(f"самое длинное слово: '{samoe_dlinnoye}' ({len(samoe_dlinnoye)} букв)")
    print(f"самое короткое слово: '{samoe_korotkoye}' ({len(samoe_korotkoye)} букв)")
    summa_dlin = 0
    for slovo in slova:
        summa_dlin += len(slovo)
    srednyaya_dlina = summa_dlin / len(slova)
    print(f"средняя длина слова: {srednyaya_dlina:.1f} букв")
    schetchik_slov = {}
    for slovo in slova:
        if slovo in schetchik_slov:
            schetchik_slov[slovo] += 1
        else:
            schetchik_slov[slovo] = 1
    sortirovannye_slova = sorted(schetchik_slov.items(), key=lambda x: x[1], reverse=True)
    top_5 = sortirovannye_slova[:5]
    print("топ-5 самых частых слов:")
    for i, (slovo, chastota) in enumerate(top_5, 1):
        print(f"{i}. '{slovo}' - {chastota} раз")