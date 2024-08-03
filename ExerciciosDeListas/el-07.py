from random import randint
from numpy import prod

numbers = [randint(1, 10) for _ in range(5)]

numbers_sum = sum(numbers)
numbers_prod = prod(numbers)

print(f'Soma: {numbers_sum}')
print(f'Multiplicação: {numbers_prod}')
print()

for i in numbers:
    print(i, end=' ') 