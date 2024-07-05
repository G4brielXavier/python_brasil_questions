from random import randint

def generate_range(qty):
    numbers = []
    n = 0
    for number in range(1, qty):
        n = randint(number, 80)
        numbers.append(n)
    return numbers

def get_size():
    size = int(input("Size: "))
    if size > 0 and size <= 20:
        return size
    else:
        print("Precisa estar dentro do limite.")
        get_size()

size = get_size()
sequence = generate_range(size)

print(f'Menor valor: {min(sequence)}')
print(f'Maior valor: {max(sequence)}')
print(f'Soma: {sum(sequence)}')