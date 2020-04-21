"""
Desenvolva um programa que pergunte a dinstância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens de até 200Km
e R$ 0,45 para viagens mais longas.
"""
km = int(input('Qual a distância da viagem (em Km): '))
value = km * 0.50 if (km <= 200) else km * 0.45
print('O valor da passagem é de R$ {:.2f}'.format(value))
