number = int(input("enter a 3 digit number:"))
reversed_number = 0
while number > 0:
    digit = number % 10
    reversed_number = (reversed_number * 10) + digit
    number = number // 10
    print("reversed number:",reversed_number)
    
