units = int(input("enter the no of units consumed"))
a=0 
if (units<100):
    a = 0
    print(a)
elif (units>100 and units<200):
    a = (units-100)*5
    print(a)
else:
    a = (units-100)*10 
    print(a)   