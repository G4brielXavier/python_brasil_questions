min_value = int(input("Min: "))
max_value = int(input("Max: "))

is_show = str(input("show number? y/n: ").lower())
is_sum = str(input("show sum? y/n: ").lower())

numbers = []

def generate_numbers(min, max, is_show, is_sum):
    for i in range(min, max + 1):
        numbers.append(i)
    
    calc = sum(numbers)
    
    if is_show == 'y' and is_sum == 'n':
        print(numbers)
    elif is_show == 'n' and is_sum == 'y':
        print(f'Soma: {calc}')
    elif is_show == 'y' and is_sum == 'y':
        print(f'Soma: {calc}')
        print(numbers)
    elif is_show == 'n' and is_sum == 'n':
        print("Sequencia Gerada!")
        
generate_numbers(min_value, max_value, is_show, is_show)