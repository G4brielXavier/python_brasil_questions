def harmonic_sum(termos):
    n = 0
    for i in range(1, termos + 1):
        n += 1 / i
    return n


termos_value = int(input("Numero de termos: "))

result = harmonic_sum(termos_value)
print(f'Soma da serie harmônica: {result:.1f}')