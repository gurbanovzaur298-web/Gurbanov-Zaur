class Frange:
    def __init__(self, start, stop=None, step=1.0):
        if stop is None:
            self.start = 0.0
            self.stop = start
        else:
            self.start = start
            self.stop = stop        
        self.step = step
        self.current = self.start    
    def __iter__(self):
        self.current = self.start
        return self  
    def __next__(self):
        if self.step > 0:
            if self.current >= self.stop:
                raise StopIteration
        else:
            if self.current <= self.stop:
                raise StopIteration
        result = self.current
        self.current += self.step
        return result
print("Frange(1, 3, 0.5):")
for x in Frange(1, 3, 0.5):
    print(x)
print("\nFrange(5, 1, -1):")
for x in Frange(5, 1, -1):
    print(x)
print("\nFrange(10):")  
count = 0
for x in Frange(10):
    print(x, end=" ")
    count += 1
    if count > 5:  
        print("...")
        break
print("\n")
print("Frange(1, 2, 0.3):")
for x in Frange(1, 2, 0.3):
    print(f"{x:.1f}")