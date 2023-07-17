def create(list):
  element = (input("enter the elements"))
  for element in element:
     list.append(element)
  return list  

def insert(list, element):
   list.append(element)
   return list
def delete(list,element):
   index = list.index(element)
   del list[index]
   return list
def sort(list):
   new_list=list[:]
   new_list.sort()
   return new_list
print("operations:\n1.create a list \n2. insert an element \n3.delete an element \n4.sort an element \n5.exit an element")
new=[]
while True:
 ch=int(input("enter the choice:"))
 if ch == 1:
    print(create(new))
 elif ch == 2:
     n=int(input("enter the element to add in the list"))
     print(insert(new,n))
 elif ch == 3:
    a = input("enter the element u want to delete")
    print(delete(new,a))
 elif ch == 4:
    print(sort(new))
 else:
    print("invalid number") 

  
 