from random import randint, uniform
from tabulate import tabulate

def generator_codes():
    qty = randint(2, 11)
    code = 0
    seq = []
    
    for i in range(0, qty + 1):
        code = f'0B{randint(1000, 6000)}'
        seq.append(code)
        
    return seq

def generator_weight(qty):
    weight = 0
    seq = []
    
    for i in range(0, len(qty) + 1):
        weight = uniform(55, 130)
        seq.append(weight)
    
    return seq 

def generator_height(qty):
    height = 0 
    seq = []
    
    for i in range(0, len(qty) + 1):
        height = uniform(1.5, 2.0)
        seq.append(height)  
        
    return seq

codes = generator_codes()
weight = generator_weight(codes)
height = generator_height(codes)

bigger_weight = max(weight)
smaller_weight = min(weight)

bigger_height = max(height)
smaller_height = min(height)

print("-------------Pesos-----------------")
print(f'{codes[weight.index(bigger_weight)]} tem o maior peso, que é de {bigger_weight:.2f}Kg')
print(f'{codes[weight.index(smaller_weight)]} tem o menor peso, que é de {smaller_weight:.2f}Kg')
print(" ")

print("------------Alturas----------------")
print(f'{codes[height.index(bigger_height)]} é o mais alto, com uma altura de {bigger_height:.2f}M')
print(f'{codes[height.index(smaller_height)]} é o mais baixo, com uma altura de {smaller_height:.2f}M')

