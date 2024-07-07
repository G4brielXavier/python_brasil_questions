from random import uniform

notas = []

for i in range(4):
    notas.append(uniform(0, 10))
    
average = sum(notas) / len(notas)
print()

for i in notas:
    print(f'{i:.1f}')
    
print()
print(f'Average: {average:.1f}')
