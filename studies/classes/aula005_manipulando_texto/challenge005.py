"""
Faça um programa que leia uma frase pelo teclado e mostre:
    Quantas vezes aparece a letra "a".
    Em que posição ela aparece a primeira vez.
    Em que posição ela aparece a última vez.
"""
frase = input('Digite uma frase: ').strip()

print('Quantidade de vezes que aparece a letra "a": {}'.format(frase.lower().count('a')))
print('A primeira letra "a" aparece na posição" {}'.format(frase.lower().find('a')))
print('A última letra "a" aparece na posição: {}'.format(frase.lower().rfind('a')))
