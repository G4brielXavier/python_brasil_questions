country_a = int(input("Country A: "))
country_b = int(input("Country B: "))

inp_percent_a = float(input("Percent A: "))
inp_percent_b = float(input("Percent B: "))

percent_a = inp_percent_a / 100
percent_b = inp_percent_b / 100

year = 0 

while country_b <= country_a:
    country_a *= (1 + percent_a)
    country_b *= (1 + percent_b)
    year += 1
    
print(f'O País B vai ultrapassar daqui a {year} anos.')