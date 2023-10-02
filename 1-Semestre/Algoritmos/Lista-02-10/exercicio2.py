while True:

    usuario = input('\nInsira seu nome de usuário: ')
    senha = input('Insira a sua senha: ')

    if (usuario == 'ElbertJean' and senha == 'Dgs589'):
        print('\nUsuário logado com sucesso')
        print('\n')
        break
    else:
        print('Erro! Por favor, verifique o nome de usuário ou senha e tente novamente!')