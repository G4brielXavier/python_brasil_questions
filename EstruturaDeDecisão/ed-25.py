ask = 0

ask_text = ["Telefonou para a vítima?", "Esteve no local do crime?", "Mora perto da vítima?", "Devia para a vítima?", "Já trabalhou com a vítima?"]
answers_ask = []


def set_ask():
    global ask, answers_ask
    
    print(f'{ask_text[ask]}')
    inpt_ask = input("[s/n]: ")
    ask += 1
    
    answers_ask.append(inpt_ask)
    if ask < 5:
        set_ask()
    else:
        print("Pesquisa concluída!!")
        
        s_answers = answers_ask.count("s")
        
        if s_answers == 2:
            print("Suspeito")
        elif s_answers == 3 or s_answers == 4:
            print("Cúmplice")
        elif s_answers == 5:
            print("Assasino")
        elif s_answers <= 1:
            print("Inocente") 

set_ask()