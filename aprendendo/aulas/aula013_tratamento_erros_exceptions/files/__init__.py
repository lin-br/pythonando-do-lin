def inserirNoArquivo(text=""):
    arquivo = open("pessoas.txt", "a")
    arquivo.write(text + "\n")
    arquivo.close()


def pegarTextoInteiroNoArquivo():
    return open("pessoas.txt", "r")
