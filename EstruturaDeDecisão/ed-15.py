side_a = float(input("Side A: "))
side_b = float(input("Side B: "))
side_c = float(input("Side C: ")) #ultimo lado

if side_a == side_b == side_c:
    print("é um equilátero")
elif side_a == side_b or side_b == side_c or side_a == side_c:
    print("é um isósceles")
elif not side_a == side_b == side_c:
    print("é um escaleno")