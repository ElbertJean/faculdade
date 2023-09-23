peso = float(input('\nInsira o seu peso. Ex: 65.7: '))
altura = float(input('Insira a sua altura: Ex: 1.75: '))

imc = peso / altura ** 2

if (imc < 20):
    print(f'\nVocê tem {peso}KGs e mede {altura}') 
    print(f'Você está abaixo do valor')
elif (imc <=25):
    print(f'\nVocê tem {peso}KGs e mede {altura}') 
    print(f'Você está no peso normal')
elif (imc <=30):
    print(f'\nVocê tem {peso}KGs e mede {altura}') 
    print(f'Você está no excesso de peso')
elif (imc <=35):
    print(f'\nVocê tem {peso}KGs e mede {altura}') 
    print(f'Você está na obesidade')
else:
    print(f'\nVocê tem {peso}KGs e mede {altura}') 
    print(f'Você está na obesidade mórbida')
