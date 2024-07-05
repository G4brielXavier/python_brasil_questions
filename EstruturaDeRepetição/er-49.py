def validation():
    n = int(input("Termos: "))
    return n

def sum_termos(n):
    seq = []
    q = 0
    for i in range(1, n + 1):
        q += i / (2 * i - 1)
    return q

termos = validation()
gen = sum_termos(termos)

print(f'A Soma dos termos: {gen:.1f}')
    