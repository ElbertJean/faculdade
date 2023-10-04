litros = int(input('Deseja abastecer quantos litros?: '))
combustivel = input('Qual combustível? E - Etanol | G - Gasolina: ')

if( (combustivel == 'e' or combustivel == 'E') and litros <=5 ):
    desconto = 3.35 * 0.965
    valorTotal = desconto * litros
    print(f'Litros abastecido = {litros}.\nDesconto de 3.5%.\nValor por litro com desconto R${desconto:.2f}. \nValor total: R${valorTotal:.2f}')
elif( (combustivel == 'e' or combustivel == 'E') and litros > 5 ):
    desconto = 3.35 * 0.95
    valorTotal = desconto * litros
    print(f'Litros abastecido = {litros}.\nDesconto de 5%.\nValor por litro com desconto R${desconto:.2f}. \nValor total: R${valorTotal:.2f}')
elif( (combustivel == 'g' or combustivel == 'G') and litros <=5 ):
    desconto = 5.25 * 0.96
    valorTotal = desconto * litros
    print(f'Litros abastecido = {litros}.\nDesconto de 4%.\nValor por litro com desconto R${desconto:.2f}. \nValor total: R${valorTotal:.2f}')
elif( (combustivel == 'g' or combustivel == 'G') and litros > 5 ):
    desconto = 5.25 * 0.92
    valorTotal = desconto * litros
    print(f'Litros abastecido = {litros}.\nDesconto de 8%.\nValor por litro com desconto R${desconto:.2f}. \nValor total: R${valorTotal:.2f}')
else: 
    print('Opção inválida, por favor, tente novamente!')