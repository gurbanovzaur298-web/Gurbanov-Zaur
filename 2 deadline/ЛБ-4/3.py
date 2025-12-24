zadachi = []
while True:
    print("\n--- мой список задач ---")
    print("1 - показать все задачи")
    print("2 - добавить задачу")
    print("3 - отметить задачу как выполненную")
    print("4 - выйти")
    vibor = input("выбери действие (1-4): ")
    if vibor == "1":
        if len(zadachi) == 0:
            print("список задач пуст")
        else:
            print("ваши задачи:")
            for i, zadacha in enumerate(zadachi, 1): 
                print(f"{i}. {zadacha}")
    elif vibor == "2":
        novaya_zadacha = input("введи описание задачи: ")
        zadachi.append(novaya_zadacha)
        print(f"задача '{novaya_zadacha}' добавлена")
    elif vibor == "3":
        if len(zadachi) == 0:
            print("нет задач для удаления")
        else:
            print("ваши задачи:")
            for i, zadacha in enumerate(zadachi, 1):
                print(f"{i}. {zadacha}")
            try:
                nomer = int(input("какую задачу выполнили (введи номер): "))
                if 1 <= nomer <= len(zadachi):
                    udalennaya = zadachi.pop(nomer - 1)
                    print(f"задача '{udalennaya}' удалена!")
                else:
                    print(f"неправильный номер (от 1 до {len(zadachi)})")
            except ValueError:
                print("введи число!")
    elif vibor == "4":
        print("выход из программы...")
        break
    else:
        print("неправильный выбор, попробуй снова")