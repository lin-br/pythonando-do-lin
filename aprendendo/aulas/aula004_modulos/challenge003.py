"""
Faça um programa que leia um ângulo qualquer e mostre
na tela o valor do seno, cosseno e tangente desse ângulo.
"""
from math import sin, cos, tan, radians

angle = float(input('Digite um ângulo: '))
radian = radians(angle)
print('Ângulo digitado: {}'.format(angle))
print('O valor do seno do ângulo é {}'.format(sin(radian)))
print('O valor do cosseno do ângulo é {}'.format(cos(radian)))
print('O valor da tangente do ângulo é {}'.format(tan(radian)))
