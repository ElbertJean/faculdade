numero = int(input('Insira a posição do Fibonacci: '))

primeiro = 0
segundo = 1
resultado = 0

if (numero <=2):
    resultado = 1
elif(numero > 2):
    for resultado in range(numero):
        resultado = primeiro + segundo
        primeiro = segundo
        segundo = resultado 

print(f'O valor Fibonacci da posição {numero} é {resultado}')
