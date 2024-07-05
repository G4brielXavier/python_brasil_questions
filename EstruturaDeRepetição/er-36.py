def validation_table():
    num_table = int(input("Tabuada do: "))
    if not num_table == 0:
        return num_table
    else:
        validation_table()
        
def validation_min():
    min = int(input("Começar por: "))
    if min >= 1 and min < 10:
        return min
    else:
        validation_min()
        
def validation_max(min):
    max = int(input("Terminar em: "))
    if max > min and max <= 10:
        return max
    else:
        validation_max()
        
def generate_table(num, min, max):
    print(f'Montando a Tabuada do {num}, começando em {min} e finalizando em {max}')
    for i in range(min, max + 1):
        print(f'{num} x {i} = {num * i}')
        
calc_num = validation_table()
min_value = validation_min()
max_value = validation_max(min_value)
generate_table(calc_num, min_value, max_value)