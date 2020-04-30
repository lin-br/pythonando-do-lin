"""
Crie um programa que leia uma frase qualquer e diga
se ela é um políndromo, desconsiderando os espaços.
Ex:
    APOS A SOPA
    A SACADA DA CASA
    A TORRE DA DERROTA
    O LOBO AMA O BOLO
    ANOTARAM A DATA DA MARATONA
"""
text = input('Digite uma frase: ').strip().upper().split()
together = ''.join(text)

# inverse = ''
# for word in range(len(together) - 1, -1, -1):
#     inverse += together[word]

# oooooou, dessa maneira mais simples:
inverse = together[::-1]

print('O inverso de {} é {}'.format(together, inverse))

if inverse == together:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
