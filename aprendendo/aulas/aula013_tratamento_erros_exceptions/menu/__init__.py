def exibirMenu():
    print('-*-' * 20)
    print('Opções disponíveis:')
    print('Digite (1) para cadastrar uma nova pessoa.')
    print('Digite (2) para listar as pessoas cadastradas.')
    print('Digite (0) para sair do programa.')
    print('-*-' * 20)


def recuperarEscolha():
    while True:
        try:
            return int(input('Escolha uma opção: '))
        except (ValueError, TypeError):
            print('Por favor digite um número.')
