"""
Crie um algoritmo que leia um número e mostre o seu dobro,
triplo e a raiz quadrada.
"""
number = float(input('Digite um número '))
print('O número digitado foi {}'.format(number))
print('O seu dobro é {}'.format(number * 2))
print('O seu triplo é {}'.format(number * 3))
# print('A sua raiz quadrada é {:.2f}'.format(number ** (1/2)))
print('A sua raiz quadrada é {:.2f}'.format(pow(number, (1 / 2))))
