import math as m

lado = int(input('\nDigite o lado do quadrado: '))
perimetro = 4 * lado
area = lado ** 2
diagonal = lado * m.sqrt(2)
print(f'\nPerimetro: {perimetro} ')
print(f'\nÁrea: {area} ')
print(f'\nDiagonal: {diagonal} ')
print('\n')