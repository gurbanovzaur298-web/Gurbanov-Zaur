from abc import ABC, abstractmethod
class PaymentSystem(ABC):
    @abstractmethod
    def pay(self, amount):
        pass    
    @abstractmethod
    def refund(self, amount):
        pass
class CreditCardPayment(PaymentSystem):
    def pay(self, amount):
        print(f"оплата картой на сумму {amount} руб.")    
    def refund(self, amount):
        print(f"возврат на карту на сумму {amount} руб.")
class PayPalPayment(PaymentSystem):
    def pay(self, amount):
        print(f"оплата через PayPal на сумму {amount} руб.")   
    def refund(self, amount):
        print(f"возврат через PayPal на сумму {amount} руб.")
try:
    ps = PaymentSystem()
    print("создали абстрактный класс")
except Exception as e:
    print(f"нельзя создать абстрактный класс: {type(e).__name__}")
print("\nработаем с конкретными классами:")
card = CreditCardPayment()
card.pay(1000)
card.refund(500)
print()
paypal = PayPalPayment()
paypal.pay(2000)
paypal.refund(300)
print()