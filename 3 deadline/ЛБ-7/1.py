from dataclasses import dataclass
@dataclass
class Product:
    name: str
    price: float
    weight: float
    is_available: bool
    def order_cost(self, quantity):
        return self.price * quantity
apple = Product("Apple", 15.0, 0.2, True)
print(f"товар: {apple}")
print(f"стоимость 10 штук: {apple.order_cost(10)}")
phone = Product("Phone", 15000.0, 0.3, True)
