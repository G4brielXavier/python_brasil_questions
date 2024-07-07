word = 'GabrielXavier'

cons = 0
voga = 0

for i in word:
    if i in ['a', 'e', 'i', 'o', 'u']:
        voga += 1
    else:
        cons += 1
        
print(f'Consoantes: {cons}')
print(f'Vogais: {voga}')