paisA = 5000
paisB = 65000

anos = 0

while paisA < paisB:
    populacaoA = paisA * 1.10
    populacaoB = paisB * 1.05
    
    paisA = populacaoA
    paisB = populacaoB

    anos += 1

print(f'Anos: {anos}')
print(f'PaisA: {paisA}')
print(f'PaisB: {paisB}')