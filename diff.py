a = {1,2,3,4,5}
b = {5,6,7,8,9,10}
c=a
for element in b:
    if element not in c:
       c.append(element)
print(c)