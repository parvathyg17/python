# f=open("sample3.txt","r")
# read = f.read()
# print(read)
# f.close()

# import os
# os.remove("sample4.txt")

# import shutil as s
# a=r"C:\Users\synnefo\Downloads\New folder (2)\kukku.txt"
# b=r"C:\Users\synnefo\Downloads"
# s.copy(a,b)

import shutil as s
a=r"C:\Users\synnefo\Downloads\New folder (2)\kukku.txt"
b=r"C:\Users\synnefo\Downloads"
s.move(a,b)