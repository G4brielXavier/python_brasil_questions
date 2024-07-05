day_week = int(input("Day of week: "))

weeks = ["sunday", "monday", "thurday", "wednesday", "thuesday", "friday", "saturday"]

if day_week in [0, 1, 2, 3, 4, 5, 6]:
    print(f'today is {weeks[day_week]}')
else:
    print("invalid number.")