while True:
    
    nota = int(input('\nInsira uma nota entre 0 e 10: '))

    if (nota >0 and nota <=10):
        print('\nNota inserida com sucesso!')
        print('\n')
        break
    else:
        print('\nPor favor, insira uma nota válida!')
