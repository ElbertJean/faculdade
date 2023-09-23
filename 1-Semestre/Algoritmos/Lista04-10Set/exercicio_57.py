import math as m

pr1 = float(input('\nDigite pr1: '))
pr2 = float(input('\nDigite pr2: '))
mf = float((pr1 + pr2) / 2)
print(f'\nMédia truncada: {round((mf-0.5) + 0.001)}')
print(f'\nMédia arredondada: {round((mf+ 0.001))}')
print('\n')