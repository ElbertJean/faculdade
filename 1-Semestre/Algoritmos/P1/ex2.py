salario = int(input('Qual o seu salário?: '))
valorVendas = int(input('Quantos de vendas fez no mês?: '))

if ( valorVendas <= 1500):
    comissao = valorVendas * 0.03
    salarioTotal = salario + comissao
    print(f'Você vendeu menos que R$ 1500.\nComissão de 3% totalizando {comissao}. \nSalario total = R$ {salarioTotal}')
elif ( valorVendas > 1500):
    comissao = valorVendas - 1500
    comissao3 = 1500 * 0.03
    comissao10 = comissao * 0.10
    salarioTotal = comissao3 + comissao10 + salario
    print(f'Você vendeu mais que R$ 1500.\nComissão de 3%: R$ {comissao3}.\nComissão de 10%: R${comissao10}.\nSalario total = R$ {salarioTotal}')
else:
    print('Valor inválido, por favor, tente novamente!') 