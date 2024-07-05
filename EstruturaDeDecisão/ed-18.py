data_format = input("Data in Calendary Format: ")

data_format_clip = data_format.split("/")

day = int(data_format_clip[0])
month = int(data_format_clip[1])
year = int(data_format_clip[2])

list_month = ["", "Janery", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

def data_aproveed(day, month, year):
    day_begin = ""
    month_begin = ""
    if day < 10:
        day_begin = "0"
    else:
        day_begin = ""
        
    if month < 10:
        month_begin = "0"
    else:
        month_begin = ""
        
    print(f'{day_begin}{day}/{month_begin}{month}/{year} - {list_month[month]} {day}, {year}')

if len(str(year)) == 4 and year <= 2024:
    if month == 4 or month == 6 or month == 9 or month == 11:
        if day <= 30:
            data_aproveed(day, month, year)
        else:
            print("Dia invalido")
    elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        if day <= 31:
            data_aproveed(day, month, year)
        else:
            print("Dia invalido")
    elif month == 2:
        if year % 4 == 0:
            if day <= 29:
                data_aproveed(day, month, year)
            else:
                print("Dia invalido")
        else:
            if day <= 28:
                data_aproveed(day, month, year)
            else:
                print("Dia invalido")