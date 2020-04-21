"""
Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome
"""
city = input('Digite o seu nome completo: ')

print('O nome possui "Silva" ? -> {}'.format('silva' in city.lower()))
