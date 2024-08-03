from random import randint

seq = []

n = 0

while not n == -1:
    n = int(input('N: '))
    seq.append(n) 

print()
print(f'Qty de valores: {len(seq)}')
print()
    
for i in seq:
    print(i, end=' ')
    
print()

seq.reverse()

for i in seq:
    print(i, end=' ')
    
print()

print(f'A Soma: {sum(seq)}')

print()

print(f'A Média: {sum(seq) / len(seq)}')

print()

count = 0
for i in seq:
    if i > sum(seq) / len(seq):
        count += 1
        
print(f'Qty. de numero > que MÉDIA: {count}')
        
print()

count_seven = 0
for i in seq:
    if i < 7:
        count_seven += 1
        
print(f'Qty. de numeros < que 7: {count_seven}')
        
print()

print('Programa encerrado com sucesso!')


