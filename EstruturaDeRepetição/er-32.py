from numpy import prod

def validation():
    n = int(input("Fatorial de: "))
    return n

def generate_fatorial(fatorial):
    current = fatorial
    seq = []
    seq.append(current)
    while current > 1:
        current -= 1
        seq.append(current)
    return seq

fat = validation()
gen = generate_fatorial(fat)

print(f'!{fat} = {gen} = {prod(gen)}')