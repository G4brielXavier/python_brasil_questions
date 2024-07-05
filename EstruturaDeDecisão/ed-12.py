per_hours = float(input("Earn p/hours: "))
hours_worked = int(input("Hours: "))

salario_bruto = per_hours * hours_worked

ir_list = ["0%", "5%", "10%", "20%"]

sindicato = salario_bruto * 0.3
inss =  0.10
fgts = 0.11
ir = 0
ir_set = ""
desconts_total = 0

if salario_bruto < 900:
    ir = 0
    ir_set = ir_list[0]
elif salario_bruto >= 900 and salario_bruto < 1500:
    ir = 0.05
    ir_set = ir_list[1]
elif salario_bruto >= 1500 and salario_bruto < 2500:
    ir = 0.1
    ir_set = ir_list[2]
elif salario_bruto >= 2500:
    ir = 0.2
    ir_set = ir_list[3]


def tabel(salario_bruto, inss, fgts, ir, ir_list, desc_total):
    desc_total = (salario_bruto * inss) + (salario_bruto * fgts) + (salario_bruto * ir)
  
    print(f'Salario Bruto: R${str(salario_bruto)}')
    print(f'IR ({ir_list}%): R${salario_bruto * ir}')
    print(f'INSS (10%): R${salario_bruto * inss}')
    print(f'FGTS (11%): R${salario_bruto * fgts}')
    print(f'Total de Descontos: R${desc_total}')
    print(f'Salario Liquido: {salario_bruto - desc_total}')
    
    
tabel(salario_bruto, inss, fgts, ir, ir_set, desconts_total)