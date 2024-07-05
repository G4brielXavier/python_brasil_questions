n = float(input("N: "))

def ver(n):
    return isinstance(n, int)

if ver(n):
    print(f'{n} é inteiro')
else:
    print(f'{n} é decimal')
