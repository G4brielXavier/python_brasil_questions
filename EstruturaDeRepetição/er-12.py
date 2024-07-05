def generate_tabuada():
    valor = int(input("Tabuada do: "))
    if valor >= 0 and valor <= 10:
        return valor
    else:
        print("O valor deve estar entre 0 e 10")

def calc_tabuada(n):
    for i in range(0, 10 + 1):
        print(f'{n} x {i} = {n * i}')
        

valor = generate_tabuada()

calc_tabuada(valor)