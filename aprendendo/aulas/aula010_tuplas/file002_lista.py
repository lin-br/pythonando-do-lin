"""
Variáveis compostas
    Tuplas inicia com ()
    Lista inicia com []
    Dicionário inicia com {}

Listas são mutáveis
"""

lanche = ['hamburguer', 'suco', 'pizza', 'pudim']
print(lanche)

lanche[3] = 'sorvete'
print(lanche)

lanche.append('cookie')
print(lanche)

lanche.insert(0, 'cachorro quente')
print(lanche)

del lanche[3]
print(lanche)

lanche.pop()
print(lanche)

lanche.pop(1)
print(lanche)

lanche.remove('suco')
print(lanche)

valores = list(range(4, 11))
print(valores)

valores.sort(reverse=True)
print(valores)

dados = list()
dados.append('Pedro')
dados.append(25)
print(dados)

pessoas = list()
pessoas.append(dados)
print(pessoas)
