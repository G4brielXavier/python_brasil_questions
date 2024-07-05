def create_turmas():
    qty = int(input("Quantas turmas?: "))
    if qty <= 10 and qty > 0:
        return qty
    else:
        create_turmas()
        
def create_alunos(turmas):
    seq = []
    
    for i in range(1, turmas + 1):
        seq.append(int(input(f'Turma {i}: ')))

    if seq.count(seq>40):
        return False

    return seq

qty_turmas = create_turmas()
alunos_turmas = create_alunos(qty_turmas)

average_turmas = []

for i in alunos_turmas:
    average_turmas.append(i / len(alunos_turmas))

print(average_turmas)