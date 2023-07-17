def max_min(list):
    max_val = list[0]
    min_val = list[0]
    for i in list:
        if i > max_val:
            max_val = i
        if i < min_val:
            min_val = i
    return max_val, min_val 
numbers = [100,55,2,45,7]
max_val, min_val=max_min(numbers)
print("maximum value:",max_val) 
print("minimum value:",min_val) 






