from random import uniform

students = 0

students_points = []
students_average = []
student_plus = 0

base = []

while students < 10:
    for i in range(4):
        base.append(uniform(0, 10))
    students_points.append(base[:])
    base.clear()
    students += 1

for i in students_points:
    students_average.append(sum(i) / 4)
    
for i in students_average:
    if i >= 7:
        student_plus += 1
        
print(f'São {student_plus} alunos com nota maior que 7.')