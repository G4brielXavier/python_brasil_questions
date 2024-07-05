from random import randint, uniform

codigo = 0
altura = 0

for i in range(1, 10 + 1):
    codigo = f'0A{randint(2000, 4000)}'
    altura = uniform(1.5, 1.95)
    
    print(f'Conjunto {i} - {codigo} - {altura:.2f}M.')