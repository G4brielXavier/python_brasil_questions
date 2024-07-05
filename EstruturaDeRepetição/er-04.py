country_a = 800000
country_b = 200000

percent_improve_a = 0.03
percent_improve_b = 0.015

year = 0

while country_a <= country_b:
    country_a *= (1 + percent_improve_a)
    country_b *= (1 + percent_improve_b)
    year += 1
    
print(f'O País ultrapassará em aproximadamente {year} anos.')
    