from random import choice
from functools import lru_cache

letter_used = ["A", "B", "C", "D", "E"]

def valid_qty_students():
    n = int(input("Quantos alunos na sala: "))
    if n > 0 and n < 41:
        return n
    else:
        valid_qty_students()
    
def valid_answer_correct(letters):
    seq = []
    for i in range(1, 10+1):
        seq.append(choice(letters))
    return seq

def gen_slots_students(qty):
    seq = []
    empty = []
    
    for i in range(0, qty + 1):
        seq.append(empty)
    return seq

@lru_cache
def gen_answers_in_empty(letters, slots, qty):
    seq = []
    count = 0 
    count_2 = 0
    base = slots
    
    while count < qty:
        while count_2 < 10:
            for i in range(0, 10):
                seq.append(choice(letters))
        base.append(seq)
    
    return base
        
    


students_qty = valid_qty_students()
correct_questions = valid_answer_correct(letter_used)
slots_empty_students = gen_slots_students(students_qty)
full_answers_students = gen_answers_in_empty(letter_used, slots_empty_students, students_qty)

print(slots_empty_students)