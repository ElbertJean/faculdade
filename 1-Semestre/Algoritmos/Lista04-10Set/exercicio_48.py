import math as m

sm = int(input('\nEntre com o salário mínimo: '))
quantidade = int(input('\nEntre com a quantidade de quilowatt: '))
preco = sm / 700
vp = preco * quantidade
vd = vp * 0.9
print(f'\nPreço do quilowatt: {preco}\nValor a ser pago: {vp}\nValor com desconto: {vd} ')
print('\n')
