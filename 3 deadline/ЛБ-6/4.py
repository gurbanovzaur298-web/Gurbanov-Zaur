import time
class Timer:
    def __enter__(self):
        self.start = time.time()
        return self    
    def __exit__(self, tip_oshibki, znachenie_oshibki, sled_oshibki):
        self.end = time.time()
        vremia = self.end - self.start
        print(f"время выполнения: {vremia:.2f} сек")
        return False
print("измеряем время сна 0.5 секунд:")
with Timer():
    time.sleep(0.5)
print("\nизмеряем время вычислений:")
with Timer():
    summa = 0
    for i in range(100000):
        summa += i
    print(f"сумма = {summa}")
print()