from random import choice
from tabulate import tabulate

nome_dos_candidatos = ["Felipe Neto", "Pablo Marçal", "Danilo Gentili"]

candidatos = {
    "Felipe Neto":0,
    "Pablo Marçal":0,
    "Danilo Gentili":0
}

def set_eleitores():
    eleitores = int(input("Eleitores: "))
    return eleitores

def generate_votes(eleitores, candidatos):
    seq = []
    voto = ""
    for i in range(1, eleitores + 1):
        voto = choice(candidatos)
        seq.append(voto)
    return seq

qty_elei = set_eleitores()
gen = generate_votes(qty_elei, nome_dos_candidatos)

for i in candidatos:
    candidatos[i] = gen.count(i)
    
resultado = [[nome_dos_candidatos[0], candidatos["Felipe Neto"]], [nome_dos_candidatos[1], candidatos["Pablo Marçal"]], [nome_dos_candidatos[2], candidatos["Danilo Gentili"]]]

print(tabulate(resultado, ["Candidatos", "Votos"], tablefmt="simple_outline"))