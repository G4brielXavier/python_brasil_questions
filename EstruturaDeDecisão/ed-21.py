def on_saque():
    qty = int(input("Withdraw: "))
    
    if not qty >= 10 and qty <= 600:
        on_saque()
    else:
        return qty

qty_saque = on_saque()

usable_notes = [100, 50, 10, 5, 1]
used_notes = {}

for nota in usable_notes:
    used_notes[nota] = qty_saque // nota
    qty_saque %= nota
    
for nota in usable_notes:
    if used_notes[nota] > 0:
        print(f'{used_notes[nota]} nota(s) de {nota} Reais')