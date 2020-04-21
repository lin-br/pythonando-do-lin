"""
Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela
a sua porção Inteira.
Ex:
    Digite um número: 6.127
    O número 6.127 tem a parte inteira 6.
"""

number = float(input('Digite um número com casas decimais: '))
# print('A parte inteira do número {} é: {}'.format(number, trunc(number)))
print('A parte inteira do número {} é: {}'.format(number, int(number)))
