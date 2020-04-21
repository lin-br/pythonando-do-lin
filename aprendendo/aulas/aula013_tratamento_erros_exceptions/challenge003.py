"""
Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo
seu nome e idade em um arquivo de texto simples. O sistema só vai ter 2 opções:
    cadastrar uma nova pessoa
    listar todas as pessoas cadastradas
"""

from aprendendo.aulas.aula013_tratamento_erros_exceptions.files import inserirNoArquivo, pegarTextoInteiroNoArquivo
from aprendendo.aulas.aula013_tratamento_erros_exceptions.menu import exibirMenu, recuperarEscolha
from aprendendo.aulas.aula013_tratamento_erros_exceptions.pessoas import cadastrar, listar

try:
    while True:
        exibirMenu()
        escolha = recuperarEscolha()
        if escolha == 1:
            nome = input('Digite o nome da pessoa: ')
            idade = int(input('Digite a idade da pessoa: '))
            inserirNoArquivo(cadastrar(nome, idade))
        elif escolha == 2:
            listar(pegarTextoInteiroNoArquivo())
        elif escolha != 0:
            print(f'Você digitou uma opção que não existe.')
        else:
            break
except KeyboardInterrupt:
    print('\n\nGAME OVER, foi um prazer jogar com você!')
