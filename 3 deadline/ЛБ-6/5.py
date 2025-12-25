class SmartList(list):
    def __getitem__(self, index):
        if index < 0:
            new_index = abs(index) - 1
            return super().__getitem__(new_index)
        else:
            return super().__getitem__(index)
sl = SmartList([10, 20, 30, 40, 50])
print(f"весь список: {sl}")
print(f"sl[0] = {sl[0]}")    
print(f"sl[-1] = {sl[-1]}")
print(f"sl[-2] = {sl[-2]}") 
print(f"sl[-3] = {sl[-3]}") 
print(f"sl[2] = {sl[2]}")    
print()