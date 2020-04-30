"""
Crie um programa que mostre na tela todos os
números pares que estão no intervalo entre 1 e 50.
"""
print('Números pares de 1 à 50:')
for number in range(1, 51):
    if number % 2 == 0:
        print(number)

# ooou:
print('Números pares de 1 à 50:')
for number in range(2, 51, 2):
    print(number)
