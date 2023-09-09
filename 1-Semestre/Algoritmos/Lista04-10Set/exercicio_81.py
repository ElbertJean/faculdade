conta = int(input('\nDigite a conta de três dígitos: '))
d1 = float(conta / 100)
d2 = float(conta % 100 // 100)
d3 = float(conta % 100 % 10)
inv = float(d3 * 100 + d2 * 10 + d1)
soma = float(conta + inv)
d1 = (soma / 100) * 1
d2 = (soma % 100 / 10) * 2
d3 = (soma % 100 % 10) * 3
digito = (d1 + d2 + d3) % 10
print(f'\nDigito verificador: {digito:.3f}')
print('\n')