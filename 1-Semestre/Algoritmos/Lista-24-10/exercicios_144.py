saldo = float(input('\nDigite o seu saldo médio: '))

if(saldo <= 500):
    print(f'Como o seu saldo é de R${saldo}, não podemos te oferecer um crédito')
elif(saldo <= 1000):
    credito = saldo * 1.30
    print(f'Como o seu saldo é de R${saldo}, podemos te oferecer um crédito de 30%. Seu crédito será de R${credito}')
elif(saldo <= 3000):
    credito = saldo * 1.40
    print(f'Como o seu saldo é de R${saldo}, podemos te oferecer um crédito de 40%. Seu crédito será de R${credito}')
else:
    credito = saldo * 1.50
    print(f'Como o seu saldo é de R${saldo}, podemos te oferecer um crédito de 50%. Seu crédito será de R${credito}')
