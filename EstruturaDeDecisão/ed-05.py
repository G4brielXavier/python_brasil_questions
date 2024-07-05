points = float(input("Your points: "))

average = 7

if points >= average:
    print("Approved!")
elif points < average:
    print("Disapproved")
elif points == average:
    print("Approved with distinction")