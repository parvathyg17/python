a = [10,5,3,8,6]
b = [15,5,3,11,9]
c = []
i = 0
while i<len(a):
    if a[i] in b:
       c.append(a[i])
    i+=1
print(c)    