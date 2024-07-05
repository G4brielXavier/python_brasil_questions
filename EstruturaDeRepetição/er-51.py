def termos(n):
    value = 0
    for i in range(1, n + 1):
        value += 1 / (2 * i - 1)
    return value

n = int(input("Numero de termos: "))

result = termos(n)

print(f'A Soma dos termos: {result:.1f}')