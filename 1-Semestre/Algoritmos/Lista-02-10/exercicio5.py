print('\nEncontre o MDC')
primeiroValor = int(input('Insira o primeiro valor: '))
segundoValor = int(input('Insira o segundo valor: '))

primeiro = 0
segundo = 0
resultado = 0

while primeiroValor % segundoValor:
    resultado = primeiroValor % segundoValor
    primeiroValor = segundoValor
    segundoValor = resultado
    
print(f'\nresultado: {resultado}')