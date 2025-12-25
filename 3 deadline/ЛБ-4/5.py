class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price   
    def __str__(self):
        return f"{self.name} - {self.price} руб."
class Order:
    def __init__(self):
        self.status = "новый"
        self.__products = []  
        self.deliverer = None  
    def add_product(self, product):
        self.__products.append(product)
        print(f"Товар '{product.name}' добавлен в заказ")  
    def set_deliverer(self, deliverer):
        self.deliverer = deliverer
        print(f"Назначен доставщик: {deliverer.name}")    
    def show_order(self):
        print(f"\nЗаказ. Статус: {self.status}")
        print("Товары:")
        total = 0
        for product in self.__products:
            print(f"  - {product}")
            total += product.price
        print(f"Итого: {total} руб.")       
        if self.deliverer:
            print(f"Доставщик: {self.deliverer.name}")
class Deliverer:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed  # скорость доставки
    def deliver(self):
        print(f"{self.name} осуществляет доставку")
class Courier(Deliverer):  # наследование
    def __init__(self, name, speed):
        super().__init__(name, speed)
    def call_client(self):
        print(f"Курьер {self.name} звонит клиенту")
    def deliver(self):  # полиморфизм
        super().deliver()
        self.call_client()
class Drone(Deliverer):  # наследование
    def __init__(self, name, speed):
        super().__init__(name, speed)    
    def fly(self):
        print(f"Дрон {self.name} летит")    
    def deliver(self):  # полиморфизм
        super().deliver()
        self.fly()
order = Order()
product1 = Product("Ноутбук", 50000)
product2 = Product("Мышь", 1500)
order.add_product(product1)
order.add_product(product2)
courier = Courier("Иван", 20)  
drone = Drone("Дрон-001", 60)  
order.set_deliverer(courier)
order.show_order()
print("\nРабота доставщиков:")
order.deliverer.deliver() 
order.set_deliverer(drone)
order.deliverer.deliver() 
print(f"\nТовар вне заказа: {product1}")