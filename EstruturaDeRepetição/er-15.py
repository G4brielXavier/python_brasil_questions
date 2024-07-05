# enesimo_termo = int(input("Termos: "))

enesimo_termo = 10 

def fibonacci(n):
    sequence = [0, 1]
    while len(sequence) < n:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
    return sequence

n = 10
gen = fibonacci(n)

print(gen)