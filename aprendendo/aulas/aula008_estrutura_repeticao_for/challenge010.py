"""
Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos.
"""

bigger = 0.00
smaller = 0.00

for number in range(0, 5):
    weight = float(input('Digite um peso: '))
    if number == 0:
        bigger = weight
        smaller = weight
    else:
        if weight > bigger:
            bigger = weight
        if weight < smaller:
            smaller = weight

print('O maior peso digitado foi {:.2f}Kg e o menor foi {:.2f}Kg'.format(bigger, smaller))
