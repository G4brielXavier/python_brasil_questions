from random import uniform

def get_atleta():
    name = input("Atleta: ")
    print(" ")
    return name

def gen_jumps():
    name_saltos = ["primeiro salto", "segundo salto", "terceiro salto", "quarto salto", "quinto salto"]
    n = 0
    saltos_miles = []
    
    for i in range(0, 5):
        n = uniform(0.2, 9.7)
        saltos_miles.append(n)
        
    for i in name_saltos:
        print(f'{i.capitalize()}: {saltos_miles[name_saltos.index(i)]:.1f}m')

    return saltos_miles

def verifying_jumps(name, jumps):
    best_jump = max(jumps)
    worse_jump = min(jumps)
    
    jumps.remove(best_jump)
    jumps.remove(worse_jump)
    
    each = 0
    for i in jumps:
        each += i
    
    print(f'Melhor salto: {best_jump:.1f}')
    print(f'Pior salto: {worse_jump:.1f}')
    print(f'Média dos demais saltos: {each / len(jumps):.1f}')
    print("-----------------------------------")
    print("Resultado Final")
    print(f'{name}: {each / len(jumps):.1f}')

name_atleta = get_atleta()
all_jumps = gen_jumps()
print("-------------------------------")
verifying_jumps(name_atleta, all_jumps)