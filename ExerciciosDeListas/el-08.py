from random import uniform, randint

peoples = []
base = []

for i in range(5):
    base.append(randint(11, 60))
    base.append(uniform(1.55, 1.9))
    peoples.append(base[:])
    base.clear()
    
peoples.reverse()

for i in peoples:
    print(i, end=' ')