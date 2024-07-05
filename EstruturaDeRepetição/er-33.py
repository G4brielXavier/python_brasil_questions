from random import uniform, randint

def generate_temperatures():
    qty = randint(2, 8)
    temperature = uniform(7, 40)
    seq = []
    seq.append(temperature)
    
    for i in range(1, qty + 1):
        temperature = uniform(7, 40)
        seq.append(temperature)
    
    return seq

def get_average(temps):
    s = 0
    for i in temps:
        s += i
    return s

temperatures = generate_temperatures()
average = get_average(temperatures)

bigger_value = max(temperatures)
smaller_value = min(temperatures)
average_value = average / len(temperatures)

print(f'A Maior temperatura registrada é de {bigger_value:.0f}°C')
print(f'A Menor temperatura registrada é de {smaller_value:.0f}°C')
print(f'A Média total é de {average_value:.0f}°C')

    