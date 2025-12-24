phone_book = {
    "Мага": "89123456789",
    "Толя": "89234567890", 
    "Стёпа": "89345678901",
    "Амир": "89456789012"
}
while True:
    print("\n--- телефонная книга ---")
    print("1 - показать все контакты")
    print("2 - добавить контакт")
    print("3 - удалить контакт")
    print("4 - выйти")
    vibor = input("выбери действие (1-4): ")
    if vibor == "1":
        print("\nвсе контакты:")
        if len(phone_book) == 0:
            print("телефонная книга пуста")
        else:
            for name, phone in phone_book.items():
                print(f"{name}: {phone}")
    elif vibor == "2":
        name_new = input("введи имя нового контакта: ").lower()
        if name_new in phone_book:
            print(f"контакт с именем '{name_new}' уже есть!")
            print(f"телефон: {phone_book[name_new]}")
        else:
            phone_new = input("введи номер телефона: ")
            phone_book[name_new] = phone_new
            print(f"контакт '{name_new}' добавлен")
    elif vibor == "3":
        name_delete = input("введи имя контакта для удаления: ").lower()
        if name_delete in phone_book:
            podtverzhdenie = input(f"точно удалить '{name_delete}'? (да/нет): ").lower()
            if podtverzhdenie == "да":
                del phone_book[name_delete]
                print(f"контакт '{name_delete}' удален")
            else:
                print("удаление отменено")
        else:
            print(f"контакта '{name_delete}' не существует")
    elif vibor == "4":
        print("выход из телефонной книги...")
        exit()  
    else:
        print("неправильный выбор, попробуй снова")