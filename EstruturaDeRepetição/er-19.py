from random import randint

def generate_numbers(qty):
    numbers = []
    n = 0
    if qty > 0 and qty <= 1000:
        while len(numbers) < qty:
            n = randint(5, 30)
            numbers.append(n)
    return numbers

size = int(input("Size: "))

sequence = generate_numbers(size)

print(sequence)