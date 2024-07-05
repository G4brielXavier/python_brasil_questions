price = float(input("Preço do Pão: "))
print("-------------------------")

def generate_table(price):
    price_bread = price
    print(f'0 - R${price_bread:.2f}')
    for bread in range(1, 50 + 1):
        price_bread += price
        print(f'{bread} - R${price_bread:.2f}')
        
generate_table(price)