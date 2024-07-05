number = []
impar = []

for i in range(1, 50 + 1):
    number.append(i)
    
for impares in number:
    if impares % 2 == 1:
        impar.append(impares)
        
print(impar)