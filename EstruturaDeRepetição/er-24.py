from random import randint

notas = int(input("Notas: "))

if notas < 20:
    seq = []
    n = 0
    qty = 0

    for i in range(1, notas + 1):
        n = randint(0, 10)
        seq.append(n)
    
    for i in seq:
        qty += i
    
    print(f'Notas: {seq}')
    print(f'A média é {qty / len(seq):.1f}')
