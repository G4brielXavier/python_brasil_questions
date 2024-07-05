from tabulate import tabulate

tabel_fruits = {
    'Fruits':["Strawberry", "Apple"],
    'Kg':[0, 0],
    'Price':[0, 0]
}



kg_strawberry = int(input("Strawberry (Kg): "))
kg_apple = int(input("Apple (Kg): "))

def ver_strawberry(kg):
    price = 0
    if kg <= 5:
        price = 2.5 * kg
    elif kg > 5:
        price = 2.2 * kg
    
    return price

def ver_apple(kg):
    price = 0
    if kg <= 5:
        price = 1.8 * kg
    elif kg > 5:
        price = 1.5 * kg
    
    return price



price_strawberry = ver_strawberry(kg_strawberry)
price_apple = ver_apple(kg_apple)

tabel_fruits['Kg'][0] = kg_strawberry
tabel_fruits['Kg'][1] = kg_apple

tabel_fruits['Price'][0] = f'R${price_strawberry}'
tabel_fruits['Price'][1] = f'R${price_apple}'

print(tabulate(tabel_fruits, headers='keys', tablefmt='fancy_grid'))