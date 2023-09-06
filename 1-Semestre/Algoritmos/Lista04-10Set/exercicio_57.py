import math as m

pr1 = float(input('\nDigite pr1: '))
pr2 = float(input('\nDigite pr2: '))
mf = (pr1 + pr2) / 2
print(f'\nMédia truncada: {int((mf-0.5) + 0.001)}')
print(f'\nMédia arredondada: {int((mf+ 0.001))}')
print('\n')