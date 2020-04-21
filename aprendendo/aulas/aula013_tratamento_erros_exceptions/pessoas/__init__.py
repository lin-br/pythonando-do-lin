def cadastrar(nome: str, idade: int):
    return nome + ";" + str(idade)


def listar(arquivoAberto):
    with arquivoAberto as arquivo:
        for linha in arquivo:
            array = linha.strip().split(";")
            print(f'Nome: {array[0]} e idade: {array[1]}')
