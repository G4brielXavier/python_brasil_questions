max_divisors = int(input("Max: "))

def create_sequence(n):
    seq = []
    
    for i in range(1, n):
        if n % i == 0:
            seq.append(i)
    
    return seq


sequence = create_sequence(max_divisors)

print(sequence)