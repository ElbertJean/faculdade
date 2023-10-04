print('Votação para presidência')
print('1 - Presidente1')
print('2 - Presidente2')
print('3 - Presidente3')
print('4 - Presidente4')
print('5 - Nulo')
print('6 - Branco')
print('0 - Finalizar votação')

presidente1 = 0
presidente2 = 0
presidente3 = 0
presidente4 = 0
nulo = 0
branco = 0
totalDeVotos = 0
finalizarVotacao = 1

while finalizarVotacao != 0: 
    
    votacao = int (input('Digite seu voto: '))
    
    finalizarVotacao = votacao

    if ( votacao == 1 ):
        presidente1 += 1
        totalDeVotos += 1
    elif( votacao == 2 ):
        presidente2 += 1
        totalDeVotos += 1
    elif( votacao == 3 ):
        presidente3 += 1
        totalDeVotos += 1
    elif( votacao == 4 ):
        presidente4 += 1
        totalDeVotos += 1
    elif( votacao == 5 ):
        nulo += 1
        totalDeVotos += 1
    elif( votacao == 6 ):
        branco += 1
        totalDeVotos += 1
    else:
        print('Valor inválido!')

porcentagemP1 = ( presidente1 * 100 ) / totalDeVotos
porcentagemP2 = ( presidente2 * 100 ) / totalDeVotos
porcentagemP3 = ( presidente3 * 100 ) / totalDeVotos
porcentagemP4 = ( presidente4 * 100 ) / totalDeVotos
porcentagemNulo = ( nulo * 100 ) / totalDeVotos
porcentagemBranco = ( branco * 100 ) / totalDeVotos

print(f'\nTotal de votos: {totalDeVotos}')
print(f'{presidente1} votos para o presidente1. Porcentagem de votos: {porcentagemP1:.1f}%')
print(f'{presidente2} votos para o presidente2. Porcentagem de votos: {porcentagemP2:.1f}%')
print(f'{presidente3} votos para o presidente3. Porcentagem de votos: {porcentagemP3:.1f}%')
print(f'{presidente4} votos para o presidente4. Porcentagem de votos: {porcentagemP4:.1f}%')
print(f'{nulo} votos nulos. Porcentagem de votos: {porcentagemNulo:.1f}%')
print(f'{branco} votos brancos. Porcentagem de votos: {porcentagemBranco:.1f}%')