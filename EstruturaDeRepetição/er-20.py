from random import randint


def set_fatorial_number():
    n_fatorial = int(input("N-Fatorial: "))
    if n_fatorial > 0 and n_fatorial <= 16:
        return n_fatorial
    else:
        set_fatorial_number()
    

def call_functions():
    n_f = set_fatorial_number()
    return n_f
        
def generate_fatorial(fatorial):
    current = fatorial
    seq = []
    seq.append(current)
    while current > 1:
        current -= 1
        seq.append(current)
        
    call_functions()
    return seq
    


nf = call_functions()
sequence = generate_fatorial(nf)

print(sequence)