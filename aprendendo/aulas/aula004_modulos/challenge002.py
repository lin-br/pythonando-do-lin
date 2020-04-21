"""
Faça um programa que leia o comprimento do cateto oposto e do cateto
adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
"""
from math import hypot

catetoOposto = float(input('Digite o comprimento do cateto oposto: '))
catetoAdjacente = float(input('Digite o comprimento do cateto adjacente: '))
print('Comprimento da hipotenusa: {:.2f}'.format(hypot(catetoOposto, catetoAdjacente)))
