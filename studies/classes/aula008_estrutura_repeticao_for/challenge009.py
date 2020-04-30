"""
Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantos já são maiores.
"""
from datetime import datetime

print('Digite o ano de nascimento de sete pessoas...')

total = 0
for x in range(0, 7):
    year = int(input('Digite o ano: '))
    if (datetime.now().year - year < 18):
        total += 1

print('Dos anos digitados, {} pessoas não atingiram a maioridade!'.format(total))
