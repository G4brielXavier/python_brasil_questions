from random import randint

candidatos = ["", "Lucas Montano", "Mano Deyvin", "Filipe Deschamps", "Fabio Akita", "Voto Nulo", "Voto em branco"]

def generate_votos():
    n = 0
    seq = []
    for i in range(0, 40 + 1):
        n = randint(1, 7)
        seq.append(n)
    return seq

def gen_candidatos_tables(cand, votos):    
    for i in range(1, 4 + 1):
        print(f'{cand[i]} - {votos.count(i)}')
        
def gen_others_tables(cand, votos):
    print("----------------------------------------")
    for i in range(5, len(cand)):
        print(f'{cand[i]} - {votos.count(i)}')
        
        
votos_values = generate_votos()

print(f'Candidatos: {len(votos_values)}')
print("---------------Resultado----------------")

gen_candidatos_tables(candidatos, votos_values)
gen_others_tables(candidatos, votos_values)

print("----------------------------------------")

voto_nulo = votos_values.count(5)
voto_em_branco = votos_values.count(6)

total_votos = len(votos_values)
percent_nulo = voto_nulo * 10
percent_branco = voto_em_branco * 10

print(f'A Porcentagem de votos nulos: {percent_nulo:.0f}%')
print(f'A Porcentagem de votos brancos: {percent_branco:.0f}%')