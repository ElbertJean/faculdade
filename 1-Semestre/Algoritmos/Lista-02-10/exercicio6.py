print('\nVerifique se o número é triangular ou não')
numero = int (input('Insira um número inteiro: '))


contador = 1
resultado = 0

while resultado < numero:
    resultado = contador * (contador + 1) * (contador +2)
    print(resultado)
    contador += 1

if resultado == numero:
    print('É um número triangular')
else:
    print('Não é um número triangular')
    