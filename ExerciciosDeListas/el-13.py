months_name = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

temps = []

for i in range(12):
    v = float(input(f'{months_name[i]}: '))
    temps.append(v)
    
average_year = sum(temps) / len(temps)
print()

for i in range(len(temps)):
    if temps[i] > average_year:
        print(f'{months_name[i]} [ {temps[i]}°C ]')
