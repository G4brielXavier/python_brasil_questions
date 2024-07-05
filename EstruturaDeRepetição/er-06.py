def side():
    use = []
    for i in range(1, 20 + 1):
        use.append(i)
    print(use)

def down():
    for i in range(1, 20 + 1):
        print(f'{i},')
        
chosse = int(input("side = 1 | down = 2: "))

match chosse:
    case 1:
        side()
    case 2:
        down()