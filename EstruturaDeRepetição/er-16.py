enesimo_termo = 500

def fibonacci(n):
    sequence = [0, 1]
    while len(sequence) < enesimo_termo:
        next_termo = sequence[-1] + sequence[-2]
        sequence.append(next_termo)
    return sequence
    
res = fibonacci(enesimo_termo)
print(res)