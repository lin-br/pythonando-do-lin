"""
Faça um programa que mostre na tela uma contagem regressiva
para o estouro de fogos de artifício, indo de 10 até 0,
com uma pausa de 1 segundo entre eles.
"""

from time import sleep

from emoji import emojize

print('Xx' * 30)
print('Contagem regressiva para os fogos de artifícios!')
print('Xx' * 30)
for number in range(10, 0, -1):
    sleep(1)
    print('Em {}'.format(number) if number > 3 else 'Em {}{}{}'.format('\033[1;31m', number, '\033[m'))
print(emojize(':boom::fireworks:' * 15, use_aliases=True))
