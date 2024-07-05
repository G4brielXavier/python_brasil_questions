def validation():
    n = int(input("Number: "))
    return n

def is_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n/2) + 1):
        if n % i == 0:
            return False
    return True

num = validation()
print(is_primo(num))