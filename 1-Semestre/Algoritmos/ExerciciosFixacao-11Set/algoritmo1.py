valor = input('Insira a sua altura (Ex: 1.75): ')
altura = float(valor.replace("," , "."))
sexo  = input('Qual o seu sexo? (M para masculino | F para feminino): ')

if (sexo.lower() == 'm'):
    calcular = (72.7* altura) - 58
    print(f'\nHomem:\nDe acordo com os dados inseridos, o seu peso ideal é {calcular:.2f}Kg')
elif (sexo.lower() == 'f'):
    calcular = (62.1* altura) - 44.7
    print(f'\nMulher:\nDe acordo com os dados inseridos, o seu peso ideal é {calcular:.2f}Kg')
else:
    print('Opção inválida')