class Multiplier:
    def __init__(self, mnozhitel):
        self.mnozhitel = mnozhitel
    def __call__(self, chislo):
        return chislo * self.mnozhitel
by_5 = Multiplier(5)
print(f"by_5(10) = {by_5(10)}")
print(f"by_5(2) = {by_5(2)}")
by_3 = Multiplier(3)
print(f"by_3(7) = {by_3(7)}")
print()