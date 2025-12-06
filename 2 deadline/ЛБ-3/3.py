phone_book = {
    'Степан В': '+7(999)391-46-67',
    'Амир Г': '+7(999)013-60-43',
    'Анатолий С': '+7(999)255-48-33',
    'Магомед кызы': '+7(999)154-23-33'
}
while True:
    print("\n" + "="*40)
    print("Телефонная книга")
    print("="*40)
    print("1 - Показать все контакты")
    print("2 - Добавить контакт")
    print("3 - Удалить контакт")
    print("4 - Выйти")
    
    choice = input("\nВыберите действие (1-4): ")
    
    if choice == '1':
        print("\nСписок контактов:")
        print("-" * 30)
        if phone_book:
            for name, phone in phone_book.items():
                print(f"{name}: {phone}")
        else:
            print("Телефонная книга пуста")
    
    elif choice == '2':
        name = input("\nВведите имя контакта: ").strip()
        if name in phone_book:
            print(f"Контакт с именем '{name}' уже существует!")
            print(f"Текущий номер: {phone_book[name]}")
            overwrite = input("Заменить? (да/нет): ").lower()
            if overwrite == 'да':
                phone = input("Введите новый номер телефона: ").strip()
                phone_book[name] = phone
                print(f"Контакт '{name}' обновлен!")
        else:
            phone = input("Введите номер телефона: ").strip()
            phone_book[name] = phone
            print(f"Контакт '{name}' добавлен!")
    
    elif choice == '3':
        name = input("\nВведите имя контакта для удаления: ").strip()
        if name in phone_book:
            del phone_book[name]
            print(f"Контакт '{name}' удален!")
        else:
            print(f"Контакт с именем '{name}' не найден!")
    
    elif choice == '4':
        print("\nВыход из программы. До свидания!")
        exit()
    
    else:
        print("\nОшибка! Пожалуйста, выберите действие от 1 до 4")