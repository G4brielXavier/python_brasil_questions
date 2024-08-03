from random import randint

numbers = [randint(2, 10) for _ in range(10)]

for i in numbers:
    i **= 2
    
print(f'A Soma dos quadrados é {sum(numbers)}')