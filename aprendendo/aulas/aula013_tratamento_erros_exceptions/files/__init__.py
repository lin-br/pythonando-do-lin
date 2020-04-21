def inserirNoArquivo(text=""):
    with open("pessoas.txt", "a") as arquivo:
        arquivo.write(text + "\n")


def pegarTextoInteiroNoArquivo():
    return open("pessoas.txt", "r")
