def create_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter
if __name__ == "__main__":
    counter = create_counter()
    print(counter())  # 1
    print(counter())  # 2
    print(counter())  # 3