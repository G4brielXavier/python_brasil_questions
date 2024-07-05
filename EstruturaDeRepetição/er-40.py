from random import randint

def generate_citycode():
    seq = []
    n = 0
    for i in range(1, 5 + 1):
        n = f'OE0{randint(3000, 5000)}'
        seq.append(n)
    return seq

def generate_cars():
    seq = []
    n = 0
    for i in range(1, 5+1):
        n = randint(500, 2000 + 1)
        seq.append(n)
    return seq

def generate_acidente():
    seq = []
    n = 0
    for i in range(1, 5 + 1):
        n = randint(15, 89)
        seq.append(n)
    return seq

code_city = generate_citycode()
cars = generate_cars()
acidentes = generate_acidente()

def show_stats(code, code_list, cars, acid):
    bigger_acid = max(acid)
    smaller_acid = min(acid)
    
    def average():
        s = 0
        for i in cars:
            s += i
        return s / len(cars)
    
    def average_acid():
        s = 0
        for i in acid:
            if i < 2000:
                s += i
        return s / len(acid)
        
    average_cars = average()
    average_acid_value = average_acid()
    
    print(f'Cidade de Codigo: {code}')
    print(f'Numero de Veiculos de passeio: {cars[code_list.index(code)]}')
    print(f'Numero de Acidentes de trânsito: {acid[code_list.index(code)]}')
    print(f'----------------------------------------------------')

    print(f'Maior índice de acidentes é na cidade de codigo {code_list[acid.index(bigger_acid)]}, com {bigger_acid} acidentes.')
    print(f'Menor índice de acidentes é na cidade de código {code_list[acid.index(smaller_acid)]}, com {smaller_acid} acidentes.')
    print(f'A Média de carros nas Cinco cidades é de {average_cars:.0f}')
    print(f'A Média de acidentes nas cidades com menos de 2000 carros: {average_acid_value:.0f}')

print(f'Codes: {code_city}')

def get_code(city):
    code = input("Escreva um dos codigos para ver: ")
    for i in city:
        if code == i:
            return code
    get_code(city)
            
code_number = get_code(code_city)
show_stats(code_number, code_city, cars, acidentes)