"""
Faça um programa que leia um número inteiro
e diga se ele é ou não um número primo.
"""
number = int(input('Digite um número para confirmar se ele é primo: '))

total = 0

for x in range(1, number + 1):
    if number % x == 0:
        print('\033[34m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print('{}'.format(x), end='\033[m ')

print('\nO número {} foi divisível {} vezes'.format(number, total))

if total == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO PRIMO!')
