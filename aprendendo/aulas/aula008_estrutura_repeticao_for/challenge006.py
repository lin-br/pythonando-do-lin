"""
Desenvolva um programa que leia o primeiro termo e a razão de uma progressão aritmética.
No final, mostre os 10 primeiros termos dessa progressão.
"""
first = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
teenth = first + (10 - 1) * razao

for x in range(first, teenth + razao, razao):
    print('{}'.format(x), end=' -> ')

print('ACABOU')
