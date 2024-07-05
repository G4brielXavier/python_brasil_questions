from random import randint

intervals = {
    "0-25":0,
    "26-50":0,
    "51-75":0,
    "76-100":0
}

def analise_interval():
    n = 0
    seq = []
    for i in range(1, 30 + 1):
        n = randint(0, 100)
        seq.append(n)
    
    
    
    for i in seq:
        if i >= 0 and i <= 25:
            intervals["0-25"] += 1
        elif i >= 26 and i <= 50:
            intervals["26-50"] += 1
        elif i >= 51 and i <= 75:
            intervals["51-75"] += 1
        elif i >= 76 and i <= 100:
            intervals["76-100"] += 1
    
analise_interval()
    
print(intervals)