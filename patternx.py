rows = 4
num = 2
for i in range(rows):
    for j in range(2, 3 * i):
        print(num, end=" ")
        num += 2
    print()
