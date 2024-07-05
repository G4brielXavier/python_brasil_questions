tamanho = float(input("Tamanho(em MB): "))
velocidade_internet = float(input("Velocidade(em Mbps): "))

tempo = tamanho / (velocidade_internet / 8)

print(f'0/{tamanho:.2f}MB | {tempo:.2f} Mbps')