text = input("Введите строку: ")

clean_text = text.lower().replace(" ", "")

left = 0
right = len(clean_text) - 1
is_palindrome = True

while left < right:
    if clean_text[left] != clean_text[right]:
        is_palindrome = False
        break
    left += 1
    right -= 1

if is_palindrome:
    print("Да, это палиндром")
else:
    print("Нет, это не палиндром")