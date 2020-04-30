"""
Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintá-la.
Sabendo que cada litro de tinta, pinta uma área de dois metros quadrados.
"""
width = float(input('Digite a largura (m): '))
height = float(input('Digite a altura (m): '))
metersQuad = width * height
print('Olá, a área dos valores digitados é {:.2f} metros quadrados.'.format(metersQuad), end=' ')
print('E a quantidade de lata de tinha necessária para pintá-la é: {:.2f}'.format(int(metersQuad / 2)))
