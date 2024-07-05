def validation():
    n = int(input("de 1 até: "))
    return n

def is_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primos(max):
    seq = []
    
    for num in range(1, max + 1):
        if is_primo(num):
            seq.append(num)
    return seq

num = validation()
gen = find_primos(num)

print(gen)        
    