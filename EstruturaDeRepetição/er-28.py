def cd():
    qty_cd = int(input("Quantidade de CD: "))
    value_cd = float(input(f'Valor dos {qty_cd} Cd: '))

    total = value_cd * qty_cd
    med_total = total / qty_cd

    return {
        "Total": total,
        "Média" : med_total
    }
    
resultado = cd()

print(f'O Valor total investido é de R${resultado["Total"]}')
print(f'A Média do valor investido é R${resultado["Média"]}')
