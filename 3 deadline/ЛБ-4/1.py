class SmartLight:
    def __init__(self):
        self.brightness = 50 
        self.color = "white"  
        self.__is_on = False  
    def turn_on(self):
        self.__is_on = True
        print("Лампа включена")   
    def turn_off(self):
        self.__is_on = False
        print("Лампа выключена")
    def set_color(self, new_color):
        self.color = new_color
        print(f"Цвет изменён на {new_color}")
    def check_status(self):
        return self.__is_on
lamp = SmartLight()
print(f"Яркость: {lamp.brightness}")
print(f"Цвет: {lamp.color}")
lamp.turn_on()
print(f"Лампа включена? {lamp.check_status()}")
lamp.set_color("синий")
print(f"Новый цвет: {lamp.color}")
