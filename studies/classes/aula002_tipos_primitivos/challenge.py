"""
Faça um programa que leia algo pelo teclado e mostre na tela
o seu tipo primitivo e todas as informações possíveis sobre ele.
"""
on = input('Digite algo:')
print('O tipo primitivo de {} é: {}'.format(on, type(on)))
print('Só tem espaços? {}'.format(on.isspace()))
print('É um número? {}'.format(on.isnumeric()))
print('É alfabético? {}'.format(on.isalpha()))
print('É alfanumérico? {}'.format(on.isalnum()))
print('Está em maiúsculas? {}'.format(on.isupper()))
print('Está em minúsculas? {}'.format(on.islower()))
print('Está capitalizada? {}'.format(on.istitle()))
