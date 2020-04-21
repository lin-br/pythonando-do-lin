def cadastrar(nome: str, idade: int):
    return nome + ";" + str(idade)


def listar(linhas):
    for linha in linhas:
        array = linha.strip().split(";")
        print(f'Nome: {array[0]} e idade: {array[1]}')
