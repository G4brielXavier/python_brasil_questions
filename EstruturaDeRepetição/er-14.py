from random import randint

numbers = []
par = []
impar = []
n = 0 

for i in range(1, 10 + 1):
    n = randint(20, 60)
    numbers.append(n)
    
for value in numbers:
    if value % 2 == 0:
        par.append(value)
    else:
        impar.append(value)
        
print(f'Pares: {len(par)}')
print(f'ímpares: {len(impar)}')