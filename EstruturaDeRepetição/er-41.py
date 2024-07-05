from tabulate import tabulate

juros = [0, 100, 150, 200, 250]
parcelas = [1, 3, 6, 9, 12]

def divida():
    n = int(input("Sua divida: "))
    if n < 5000 and n > 500:
        return n
    else:
        divida()
        
def generate_juros(div, jur):
    seq = []
    current = div
    n = 0
    for i in jur:
        n = current + i
        seq.append(n)
    return seq 

def generate_parcelas(jur_div, parcel):
    seq = []
    n = 0
    for i in jur_div:
        for parcela in parcel:
            n = i / parcela
            seq.append(int(n))
            
    return seq


div_num = divida()
juros_list = generate_juros(div_num, juros)
parcelas_list = generate_parcelas(juros_list, parcelas)

print("Divida      Juros      Parcelas    Resultado")
for i in range(0, 4+1):
    print(f'R${juros_list[i]}      {juros[i]}          {parcelas[i]}          R${parcelas_list[i]}')