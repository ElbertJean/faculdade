litros = float(input('Quantos litros você comprou?: '))
combustivel  = input('Qual combustível? (A para álcool | G para gasolina): ')

if (combustivel.lower() == 'a' and litros <= 20 ):
    desconto = 