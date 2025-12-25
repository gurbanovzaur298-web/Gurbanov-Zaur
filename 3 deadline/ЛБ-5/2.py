class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder 
        self.balance = balance   
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Пополнение на {amount} руб. Баланс: {self.balance} руб.")
        else:
            print("Ошибка: сумма должна быть положительной")
    def withdraw(self, amount):
        if amount <= 0:
            print("Ошибка: сумма должна быть положительной")
        elif amount > self.balance:
            print("Недостаточно средств!")
        else:
            self.balance -= amount
            print(f"Снятие {amount} руб. Баланс: {self.balance} руб.")   
    def get_balance(self):
        return self.balance
account = BankAccount("Иванов", 100)
print(f"Владелец: {account.account_holder}")
print(f"Начальный баланс: {account.get_balance()} руб.")
account.deposit(50)
account.withdraw(200) 
account.withdraw(30)
print(f"Итоговый баланс: {account.get_balance()} руб.")
account2 = BankAccount("Петров")
print(f"\nНовый счёт для {account2.account_holder}")
print(f"Баланс: {account2.get_balance()} руб.")
account2.deposit(1000)
account2.withdraw(300)
print(f"Баланс после операций: {account2.get_balance()} руб.")