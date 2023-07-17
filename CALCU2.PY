def sum():
    a=int(input("enter the number:"))
    b = int(input("enter the number:"))
    print(a+b)
def sub():
    a=int(input("enter the number:"))
    b = int(input("enter the number:"))
    print(a-b)
def mul():
    a=int(input("enter the number:"))
    b = int(input("enter the number:"))
    print(a*b)
def div():
    a=int(input("enter the number:"))
    b = int(input("enter the number:"))
    print(a/b)    
while True:
    ch = int(input("Enter the choice:"))
    if ch == 1:
        sum()
    elif ch == 2:
        sub()
    elif ch == 3:
        mul()
    elif ch == 4:
        div()
    elif ch == 5:
        print("invalid choice")
        break
    