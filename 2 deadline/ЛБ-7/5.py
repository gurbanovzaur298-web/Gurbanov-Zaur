def format_report(report_title: str, *data: str, **properties: str) -> None:
    print(f"--- Отчет: {report_title} ---")
    print("Данные:")
    if data:
        for item in data:
            print(f" - {item}")
    else:
        print(" - Нет данных")
    print("\Свойства:")
    if properties:
        for key, value in properties.items():
            print(f" - {key}: {value}")
    else:
        print(" - Нет свойств")
    print("------------------------------")
format_report(
    "Ежедневный отчет",
    "Продажи выросли на 10%",
    "Новых клиентов: 5",
    author="Сидоров А.В.",
    date="2025-11-04"
)