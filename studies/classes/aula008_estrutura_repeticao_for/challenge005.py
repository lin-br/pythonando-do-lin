"""
Desenvolva um programa que leia seis números inteiros
e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-o
"""
total = 0
for number in range(0, 6):
    inp = int(input('Digite um número: '))
    total += inp if (inp % 2 == 0) else 0

print('Soma total dos números digitados: {}'.format(total))
