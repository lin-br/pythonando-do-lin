"""
Refaça o desafio da tabuada de um número
que o usuário digitar utilizando o laço for.
"""
inp = int(input('Digite um número para exibir a tabuada: '))

print('=-' * 20)

for number in range(1, 11):
    print('{} x {} = {}'.format(inp, number, inp * number))
