class CreditCard:
    def __init__(self, number, cvc, owner_name):
        self.__number = number 
        self.__cvc = cvc       
        self.owner_name = owner_name  
        self._balance = 1000.0 
    
    def pay(self, amount, pin):
        if self.__check_pin(pin): 
            if amount <= self._balance:
                self._balance -= amount
                print(f"Оплачено {amount} руб. Остаток: {self._balance} руб.")
                return True
            else:
                print("Недостаточно средств")
                return False
        else:
            print("Неверный PIN-код")
            return False
    def __check_pin(self, pin):
        return pin == "1234"
    def get_balance(self):
        return self._balance
card = CreditCard("1234-5678-9012-3456", "123", "Иван Иванов")
print(f"Владелец: {card.owner_name}")
print(f"Баланс: {card.get_balance()} руб.")
card.pay(200, "1234") 
card.pay(300, "0000")  