from tabulate import tabulate

def creating_table():
    qty_items = 50
    price_items = 1.99
    
    qty_seq = []
    qty_price_seq = []
    
    for i in range(1, qty_items + 1):
        price_items += 1.99
        print(f'{i} - R${price_items:.2f}')
        
        
    return {
        "Quantidade": qty_seq,
        "Preços": qty_price_seq
    }
    
resultado = creating_table()