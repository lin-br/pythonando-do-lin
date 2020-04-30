"""
Escreva um programa que faça o computador "pensar" em um número inteiro
entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido
pelo computador.

O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""
from random import randint

import emoji

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)

numberPerson = int(input('Em que número eu pensei? '))
numberMachine = randint(0, 5)

if numberPerson == numberMachine:
    print(emoji.emojize('Você ganhou! :sunglasses: \nEu pensei no número {}', use_aliases=True).format(numberMachine))
else:
    print(emoji.emojize('Você perdeu :disappointed: \nEu pensei no número {}', use_aliases=True).format(numberMachine))
