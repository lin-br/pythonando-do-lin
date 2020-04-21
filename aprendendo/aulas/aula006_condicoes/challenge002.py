"""
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada KM acima do limite.
"""

vel = int(input('Qual a velocidade do carro? '))
limitVelocity = 80

if vel > limitVelocity:
    print('Você foi multado! O valor da sua multa ficou R$ {:.2f}'.format((vel - limitVelocity) * 7))
else:
    print('Continue seguindo o limite de velocidade!')
