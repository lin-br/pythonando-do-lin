def soma(a, b):
    print(f'Estou somando {a} + {b} que é igual a {a + b}')


def contador(*n):  # com o * recebe uma lista ou tupla
    for valor in n:
        print(f'{valor}', end=' ')
    print('PAREI DE CONTAR...')


def contador(**mapp):  # com o ** recebe um dicionário -> chave = valor
    for key, value in mapp:
        print(f'A chave {key} tem o valor {value}')


def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


soma(4, 5)

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

valores = [7, 2, 5, 0, 4]
print(f'Valores não dobrados: {valores}')

dobra(valores)
print(f'Valores dobrados: {valores}')

"""
existe uma função de ajuda para exibir o manual completo de uma função em Python
eles chamam de interactive help..

É possível executar no console do python: help()
Ou em um arquivo python: help()
Ou melhor ainda o help com o nome da função: help(print)
"""
help(print)

"""
Existe também um comando para exibir o doc de um comando, atribuindo "__doc__" no método:
input.__doc__
print.__doc__
len.__doc__
"""
print(input.__doc__)


def somar(a, b, c=0):
    print(f'A soma vale: {a + b + c} (com parâmetro opcional)')


somar(3, 2, 5)
somar(8, 4)


def somarComRetorno(a, b, c):
    return a + b + c


print(f'Somando com o retorno {somarComRetorno(3, 2, 5)}')
