points = float(input("yours points: "))

rank = ""

if points >= 0 and points <= 4:
    rank = "E"
elif points > 4 and points < 6:
    rank = "D"
elif points >= 6 and points < 7.5:
    rank = "C"
elif points >= 7.5 and points < 9:
    rank = "B"
elif points >= 9 and points < 10:
    rank = "A"
elif points == 10:
    rank = "S"
    
if rank == "S":
    print("Excellent")
elif rank == "A" or rank == "B" or rank == "C":
    print("Aprovved")
elif rank == "D" or rank == "E":
    print("Disaprovved")
    