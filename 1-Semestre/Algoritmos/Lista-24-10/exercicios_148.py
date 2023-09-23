op = int(input('Digite 1- Região Norte | 2- Região Nordeste | 3- Região Centro-Oeste | 4- Região Sul \nSua resposta: '))
iv = int(input('Digite 1- Ida | 2- Ida e volta\n Sua resposta: '))

if (op == 1):
    if(iv == 1):
        print('O valor da passagem de ida para R.Norte é R$500,00')
    elif(iv == 2):
        print('O valor da passagem de ida-volta para R.Norte é R$ 900,00')
    else:
        print('Você inseriu uma opção inválida')
elif (op == 2):
    if(iv == 1):
        print('O valor da passagem de ida para R.Nordeste é R$350,00')
    elif(iv == 2):
        print('O valor da passagem de ida-volta para R.Nordeste é R$ 650,00')
    else:
        print('Você inseriu uma opção inválida')
elif (op == 3):
    if(iv == 1):
        print('O valor da passagem de ida para R.Centro-Oeste é R$350,00')
    elif(iv == 2):
        print('O valor da passagem de ida-volta para R.Centro-Oeste é R$ 600,00')
    else:
        print('Você inseriu uma opção inválida')
elif (op == 4):
    if(iv == 1):
        print('O valor da passagem de ida para R.Sul é R$350,00')
    elif(iv == 2):
        print('O valor da passagem de ida-volta para R.Sul é R$ 550,00')
    else:
        print('Você inseriu uma opção inválida')
else:
    print('Você inseriu uma opção inválida')