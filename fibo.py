def fibonacci(n):
    if n<=0:
        return[]
    elif n==1:
        return[0]
    elif n==2:
        return[0,1]
    else:
        sequence=fibonacci(n-1)
        sequence.append(sequence[-1]+sequence[-2])
        return sequence
n=int(input("enter a number:"))
fib_sequence=fibonacci(n)
print("fibonacci series:",fib_sequence)