product_1 = float(input("Product 1: "))
product_2 = float(input("Product 2: "))
product_3 = float(input("Product 3: "))

cheaper_price = min(product_1, product_2, product_3)

print(f'Among these products, the cheapest price is R${cheaper_price}')