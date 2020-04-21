"""
Faça um programa que leia um número inteiro e mostre
na tela o seu sucessor e seu antecessor.
"""
number = int(input('Digite um número inteiro: '))
print(
    'O número digitado foi {}, o seu antecessor é {} e o seu sucessor é {}.'.format(number, (number - 1), (number + 1)))
