items = ["Cachorro Quente", "Bauru simples", "Bauru com ovo", "Hamburguer", "Cheeseburguer", "Refrigerante"]
price_fmt = ["1,20", "1,30", "1,50", "1,20", "1,30", "1,00"]
price = [1.2, 1.3, 1.5, 1.2, 1.3, 1]

print("----- Menu -----")
for name in items:
    print(f'{items.index(name)} - {name} - R${price_fmt[items.index(name)]}')

print("------------------------------------")

def get_order(menu):
    print("Escreva o numero do pedido que deseja.")
    order = input("Faça seu pedido separado por espaços \n : ")
    order_num = order.split(" ")
    
    order_list = []
    
    for order in order_num:
        order_list.append(menu[int(order)])
    
    return order_list

def get_qty_order(orders):
    print("------------------------")
    print(f'Você escolheu {orders}')
    print("Separe a quantidade por espaços")
    qty = input("Quanto de cada você vai querer?: ")
    qty_orders = qty.split(" ")
    return qty_orders

def show_order(menu, orders, qty, price):
    print("-------------------------")
    price_order = 0
    total_order = 0

    for i in range(0, len(orders)):
        price_order = price[menu.index(orders[i])] * int(qty[i])
        total_order += price_order
        print(f'{qty[i]}x - {orders[i]} - R${price_order}')
    
    print("---------------------------")
    print(f'Total á pagar: R${total_order}')
    

order_value = get_order(items)
qty_orders_value = get_qty_order(order_value)
show_order(items, order_value, qty_orders_value, price)

