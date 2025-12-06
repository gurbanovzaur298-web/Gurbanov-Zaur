symbol = input("Введите символ: ")
height = int(input("Введите высоту: "))
width = int(input("Введите ширину: "))

row = 0
while row < height:
    col = 0
    line = ""
    
    while col < width:
        line += symbol
        col += 1
    
    print(line)
    row += 1