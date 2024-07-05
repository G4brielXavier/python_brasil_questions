from random import randint, uniform

print("----Lojas SUPER----")

def generate_clients():
    n = randint(1, 10)
    return n

def set_buy_items(client_qty):
    price = 0
    seq = []
    for items in range(1, client_qty + 1):
        price = uniform(0, 9)
        print(f'Produto {items} - R${price:.2f}')
        seq.append(price)
    return seq

qty = generate_clients()
s = set_buy_items(qty)
print("_____________________________")

total = 0

for i in s:
    total += i

dinheiro = uniform(total, 100)
troco = dinheiro - total

    
print(f'Valor á Pagar: R${total:.2f}')
print(f'Dinheiro: R${dinheiro:.2f}')
print(f'Troco: R${troco:.2f}')
print("_______________________________")
print("Obrigado, volte sempre.")