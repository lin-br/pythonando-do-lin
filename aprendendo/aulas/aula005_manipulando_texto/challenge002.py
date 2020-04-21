"""
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
Ex:
    Digite um número: 1834
---
    unidade:4
    dezena: 3
    centena: 8
    milhar: 1
"""

# Do jeito que eu fiz
number = input('Digite um número de 0 a 9999: ')

print('Milhar: {}'.format(number[0]))
print('Centena: {}'.format(number[1]))
print('Dezena: {}'.format(number[2]))
print('Unidade: {}'.format(number[3]))

# Do jeito que o cara fez
number = int(input('Digite um número de 0 a 9999: '))
unidade = (number // 1) % 10
dezena = (number // 10) % 10
centena = (number // 100) % 10
milhar = (number // 1000) % 10

print('Analisando o número: {}'.format(number))
print('Milhar: {}'.format(milhar))
print('Centena: {}'.format(centena))
print('Dezena: {}'.format(dezena))
print('Unidade: {}'.format(unidade))
