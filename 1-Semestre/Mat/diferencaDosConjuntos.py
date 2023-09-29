print(f'\n\nSegundo programa de matemática discreta')
print(f'Diferença dos conjuntos')
print(f'Retirar do primeiro conjunto A a intersecção de A e B')
print('\n')

def diferenca(a, b):
    diferenca = a - b
    return diferenca

conjuntoA = set(input(f"Informe os elementos do conjunto A separados por espaço: ").split())
conjuntoB = set(input(f"Informe os elementos do conjunto B separados por espaço: ").split())

resultado = diferenca(conjuntoA, conjuntoB)

print(f"\nA diferença do conjunto A para o conjunto B é: {resultado}")
