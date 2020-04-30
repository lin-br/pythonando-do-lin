"""
Código em ANSI:
Sempre começa com -> \033[
Sempre finaliza com -> m

style -> código do estilo do texto
    Os que funcionando melhor com o padrão ANSI (que o Python é compátivel):
        0 - NONE
        1 - BOLD (negrito)
        4 - UNDERLINE
        7 - NEGATIVE (vai inverter)
text -> código do texto
    Exemplos do padrão ANSI(se quiser mais cores, necessário bibliotecas):
        30 - branco
        31 - vermelho
        32 - verde
        33 - amarelo
        34 - azul
        35 - lilás
        36 - verde água
        37 - cinza (cor padrão)
back -> código do fundo
    Exemplos do padrão ANSI(se quiser mais cores, necessário bibliotecas):
        40 - branco
        41 - vermelho
        42 - verde
        43 - amarelo
        44 - azul
        45 - lilás
        46 - verde água
        47 - cinza (cor padrão)

O código é formado:

            style       back
        \033[   :     :     m
                text
Exemplo:
style = 0
text = 33
back = 44

            style    back
        \033[ 0: 33: 44 m
                text
"""

print('\033[1;31;43mOlá, Mundo!')
print('\033[1;31;43mOlá, Mundo!\033[m')
print('\033[4;30;45mOlá, Mundo!\033[m')
print('Os valores são \033[32m{} e \033[31m{}\033[m'.format(3, 5))
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m'.format(3, 5))
print('Olá {}{}{}!'.format('\033[4;34m', 'Lin', '\033[m'))
