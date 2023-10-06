numero = int(input('Insira um número e verifique se ele é divisivel por 2: '))

resultado = 0

while resultado % 2 == 0:
    resultado = numero % 2
    print(resultado)
    break

if resultado == 0:
    print(f'É divisivel por 2 com resto {resultado}')
else:
    print(f'Não é divisivel por 2 com resto {resultado}')