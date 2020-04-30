"""
Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente.
Ex:
    Ana Maria de Souza
---
    primeiro = Ana
    último = Souza
"""
name = input('Digite um nome completo: ').strip()
splited = name.split()

print('Primeiro nome: {}'.format(splited[0]))
print('Último nome: {}'.format(splited[-1]))
# ou dessa maneira aqui também:
print('Último nome: {}'.format(splited[len(splited) - 1]))
