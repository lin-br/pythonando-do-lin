"""
Escreva um programa que converta uma temperatura digitada em
ºC e converta para ºF.
"""
celsius = float(input('Digite a temperatura em ºC: '))
print('A temperatura de {}ºC corresponde a {}ºF'.format(celsius, (((9 * celsius) / 5) + 32)))
