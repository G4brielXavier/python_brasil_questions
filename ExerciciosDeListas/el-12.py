from random import randint, uniform

student = []
base = []

for i in range(30):
    base.append(randint(9, 20))
    base.append(uniform(1.5, 2.0))
    
    student.append(base[:])
    base.clear()
    
sum_value = 0
count = 0

for i in student:
    sum_value += i[1]
    
average = sum_value / len(student)

for i in student:
    if i[0] > 13:
        if i[1] < average:
            count += 1
            
print(f'São {count} alunos.')
