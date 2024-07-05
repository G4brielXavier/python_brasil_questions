from numpy import prod

n_fatorial = int(input("n-fatorial: "))

numbers = []

current_fatorial = n_fatorial
previous_fatorial = 0

numbers.append(n_fatorial)

while current_fatorial > 1:
    current_fatorial -= 1
    previous_fatorial = current_fatorial - 1
    numbers.append(current_fatorial)
    
print(f'!{n_fatorial} = {numbers} = {prod(numbers)}')