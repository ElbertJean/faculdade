print(f'\n\nQuarto programa de matemática discreta')
print(f'Proposição')
print(f'Permite realizar o login se as duas informações forem verdadeiras')
print('\n')

while True:

    nome = input('\nInsira o seu nome de usuário: ')
    senha = input('Insira a sua senha: ')

    if ( nome == 'Elbert'):
        if (senha == 'dgs589'):
            print('Você está logado!\n')
            break
        else:
            print('Senha inválida\n')
    else:
        print('Usuário inválido\n')