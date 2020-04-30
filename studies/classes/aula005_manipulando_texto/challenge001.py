"""
Crie um programa que leia o nome completo de uma pessoa e mostre:
    O nome com todas as letras maiúsculas
    O nome todas as letras minúsculas
    Quantidade de letras sem considerar espaços
    Quantas letras tem o primeiro nome
"""
name = input('Digite o nome completo: ')
print('Todas as letras maiúsculas: {}'.format(name.upper()))
print('Todas as letras minúsculas: {}'.format(name.lower()))
print('Quantidade de letras sem os espaços: {}'.format(len(name.replace(' ', ''))))
print('Quantidade de letras no primeiro nome({}): {}'.format(name.split()[0], len(name.split()[0])))
