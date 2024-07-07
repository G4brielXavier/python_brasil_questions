from random import uniform

seq = []

for i in range(10):
    seq.append(uniform(1, 10))
    
print(seq[:-1])