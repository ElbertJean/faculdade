nome = input('\nInsira o seu nome: ')
idade = int(input('Qual a sua idade?: '))

if(idade <= 10):
    print(f'\n{nome} pagará R$30,00')
elif(idade > 10 and idade <=29):
    print(f'\n{nome} pagará R$60,00')
elif(idade > 29 and idade <=45):
    print(f'\n{nome} pagará R$120,00')
elif(idade > 45 and idade <=59):
    print(f'\n{nome} pagará R$150,00')
elif(idade > 59 and idade <=65):
    print(f'\n{nome} pagará R$250,00')
else:
    print(f'\n{nome} pagará R$400,00')
