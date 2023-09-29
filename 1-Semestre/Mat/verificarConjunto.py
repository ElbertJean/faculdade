print(f'\n\nQuinto programa de matemática discreta')
print(f'Intersecção')
print(f'Verifica a intersecção dos conjuntos A e B')
print('\n')

conjuntoA = set(input(f"Informe os elementos do conjunto A separados por espaço: ").split())
conjuntoB = set(input(f"Informe os elementos do conjunto B separados por espaço: ").split())

interseccao = conjuntoA.intersection(conjuntoB)

if interseccao:
    print(f'A interseção entre os conjuntos é: {interseccao}')
else:
    print(f'Não há elementos em comum nos conjuntos.')
