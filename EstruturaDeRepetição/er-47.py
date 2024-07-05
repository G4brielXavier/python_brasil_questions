from random import uniform

name = input("Atleta: ")

def gen_points_jurors():
    n = 0
    seq = []
    for i in range(0, 7):
        n = uniform(0, 10)
        seq.append(n)
        print(f'Nota {i} - {n:.1f}')
    return seq

points = gen_points_jurors()
print(" ")
print("Resultado Final")
print(f'Atleta: {name}')
print(f'Melhor nota: {max(points):.1f}')
print(f'Menor nota: {min(points):.1f}')

points.remove(max(points))
points.remove(min(points))
total = 0
for i in points:
    total += i
    
print(f'Média: {total / len(points):.1f}')
        
        

        
