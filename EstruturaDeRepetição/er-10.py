limit_min = int(input("Min: "))
limit_max = int(input("Max: "))

numbers = []

for i in range(limit_min, limit_max + 1):
    numbers.append(i)
    
print(numbers)