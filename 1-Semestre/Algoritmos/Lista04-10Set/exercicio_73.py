num = float(input('\nEntre com um número com parte fracionária: '))
numi = round(num - 0.5)
numfrac = num - numi
numa = round(num + 0.00001)
print(f'\nParte inteira: {numi}')
print(f'\nParte fracionária: {(numfrac + 0.00001):.3f}')
print(f'\nParte arredondado: {numa}')
print('\n')