"""
Faça um programa que calcule a soma entre todos os números ímpares
que são múltiplicos de três e que se encontram no intervalo de 1 até 500.
"""
amount = 0
for number in range(1, 501):
    if (number % 2 != 0) and (number % 3 == 0):
        print('Número é: {}'.format(number))
        amount += number
print('Resultado da soma: {}'.format(amount))
