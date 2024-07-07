from random import randint

main_seq = []
pairs = []
inpairs = []

for _ in range(20):
    main_seq.append(randint(1, 50))
    
for i in main_seq:
    if i % 2 == 0:
        pairs.append(i)
    else:
        inpairs.append(i)
        
print(main_seq)
print(pairs)
print(inpairs)