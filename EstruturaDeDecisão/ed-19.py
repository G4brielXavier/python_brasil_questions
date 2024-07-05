n = input("Type it a number(<1000): ")

if int(n) < 1000:
    centena = n[0]
    dezena = n[1]
    unidade = n[2]
    
    print(f'{centena} Centenas, {dezena} Dezenas e {unidade} Unidades.')