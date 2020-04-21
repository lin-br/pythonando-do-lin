"""
Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
"""
from datetime import date

year = int(input('Digite um ano para verificar se é bissexto (digite 0 para o ano atual): '))
year = date.today().year if year == 0 else year
isLeapYear = year % 4 == 0 and year % 100 != 0 or year % 400 == 0

if isLeapYear:
    print('O ano digitado ({}) é bissexto!'.format(year))
else:
    print('O ano digitado ({}) não é bissexto :/'.format(year))
