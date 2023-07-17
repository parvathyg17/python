a = input("enter a string")
b = ""
i = len(a)-1
while i >=0:
    b += a[i]
    i -= 1
print(b)