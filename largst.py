a = [11,13,12,7,8,9,14,18]
b = []
i = 0
while i < len(a):
    if a[i] % 2 == 0:
        b.append(a[i])
    i += 1
print(b)
