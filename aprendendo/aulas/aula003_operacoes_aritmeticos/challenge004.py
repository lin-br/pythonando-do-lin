"""
Escreva um programa que leia um valor em metros e o
exiba convertido em centímetros e milímetros.
"""
meters = float(input('Metros para serem convertidos: '))
print('Você digitou {} metros, esse valor em centímetros é {:.0f} e em milímetros é {:.0f}'.format(meters, meters * 100,
                                                                                                   meters * 1000))
