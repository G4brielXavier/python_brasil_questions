wage = float(input("your wage: "))

percents_list = ["20%", "15%", "10%", "5%"]
percents_for_calc = [0.2, 0.15, 0.1, 0.05]

def for_calc(wage, per_calc, per_print):
    improve = wage * per_calc
    
    print(f'After wage: R${wage}')
    print(f'Percent Aplicated: {per_print}')
    print(f'Improved value: R${improve}')
    print(f'Your new wage: R${wage + improve}')


if wage < 280:
    for_calc(wage, percents_for_calc[0], percents_list[0])
elif wage >= 280 and wage < 700:
    for_calc(wage, percents_for_calc[1], percents_list[1])
elif wage >= 700 and wage < 1500:
    for_calc(wage, percents_for_calc[2], percents_list[2])
elif wage >= 1500:
    for_calc(wage, percents_for_calc[3], percents_list[3])
    