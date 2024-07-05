
def average(value):
    return value / 5

def sum(n1, n2, n3, n4, n5):
    return n1 + n2 + n3 + n4 + n5


n1 = float(input("n1: "))
n2 = float(input("n2: "))
n3 = float(input("n3: "))
n4 = float(input("n4: "))
n5 = float(input("n5: "))


sum_value = sum(n1, n2, n3, n4, n5)
average_value = average(sum_value)

print(f'A soma: {sum_value}')
print(f'A Média: {average_value:.2f}')