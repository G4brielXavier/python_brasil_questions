def bigger(n1, n2, n3, n4, n5):
    return max(n1, n2, n3, n4, n5)


n1 = float(input("n1: "))
n2 = float(input("n2: "))
n3 = float(input("n3: "))
n4 = float(input("n4: "))
n5 = float(input("n5: "))

res = bigger(n1, n2, n3, n4, n5)
print(f'O Maior numero é {res}')