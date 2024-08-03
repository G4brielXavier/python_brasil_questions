asks = ['Telefonou para a vítima?', 'Esteve no local do crime?', 'Mora perto da vítima?', 'Devia para a vítima?', 'Já trabalhou com a vítima?']

yes = 0

for i in range(len(asks)):
    v = input(f'{asks[i]} [y/n]: ')

    if v in ['y', 'n']:
        if v == 'y':
            yes += 1
        else:
            pass
    else:
        print('Y or N')

if yes == 2:
    print('Suspeita')
elif yes >= 3 and yes <= 4:
    print('Cúmplice')
elif yes == 5:
    print('Assasino')
else:
    print('Inocente')
        


    