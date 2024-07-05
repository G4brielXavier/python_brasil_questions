def is_primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def get_divisors(n):
    seq_divisors = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            seq_divisors.append(i)
            seq_divisors.append(n // i)
    return seq_divisors

def main():
    n = int(input("Numero: "))
    
    if is_primo(n):
        print(f'{n} é um numero primo.')
    else:
        print(f'{n} não é numero primo.')
        print(f'Os divisores são {get_divisors(n)}')
        
main()