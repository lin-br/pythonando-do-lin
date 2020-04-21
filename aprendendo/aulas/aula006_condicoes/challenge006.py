"""
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
"""
numberOne = int(input('Digite o primeiro número: '))
numberTwo = int(input('Digite o segundo número: '))
numberThree = int(input('Digite o terceiro número: '))

maxx = numberOne
if numberTwo > maxx:
    maxx = numberTwo
if numberThree > maxx:
    maxx = numberThree

minu = numberOne
if numberTwo < minu:
    minu = numberTwo
if numberThree < minu:
    minu = numberThree

print('O número maior digitado é: {}'.format(maxx))
print('O número menor digitado é: {}'.format(minu))
