def sum_digits(number):
    if number < 10:
        return number  
    last_digit = number % 10  
    remaining = number // 10     
    return last_digit + sum_digits(remaining)
print( sum_digits(12345)) 
 