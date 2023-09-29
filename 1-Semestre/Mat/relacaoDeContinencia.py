print(f'\n\nTerceiro programa de matemática discreta')
print(f'Relacao de Continência')
print(f'Relação de conjunto para conjunto. A está contido em B?')
print('\n')

conjuntoA = set(input(f"Informe os elementos do conjunto A separados por espaço: ").split())
conjuntoB = set(input(f"Informe os elementos do conjunto B separados por espaço: ").split())

# A função issubset verifica se todos os itens do conjunto existem no conjunto especificado
# https://www.w3schools.com/python/ref_set_issubset.asp

if conjuntoA.issubset(conjuntoB):
    print("\nConjunto A está contido em B.")
else:
    print("\nConjunto A não está contido em B.")