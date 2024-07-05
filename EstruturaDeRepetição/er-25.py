from random import randint

def ask_peoples():
    peoples = int(input("Peoples: "))
    if peoples > 0 and peoples <= 40:
        return peoples
    else:
        ask_peoples()

def generate_ages(peoples):
    ages = []
    r = 0
    for i in range(1, peoples + 1):
        r = randint(18, 65)
        ages.append(r)
    return ages

def verify_ages(ages):
    seq_smallers = []
    seq_biggers = []
    
    for i in ages:
        if i > 0 and i <= 26:
            seq_smallers.append(i)
        elif i > 26:
            seq_biggers.append(i)
            
    return seq_smallers, seq_biggers
        


people = ask_peoples()
ages_seq = generate_ages(people)
result_verify = verify_ages(ages_seq)

grandpas = len(result_verify[1])
kid = len(result_verify[0])

if grandpas > kid:
    print(f'Uma turma idosa')
else:
    print(f'Uma turma adulta')