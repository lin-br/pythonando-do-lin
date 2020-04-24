"""
Variáveis compostas
    Tuplas inicia com ()
    Lista inicia com []
    Dicionário inicia com {}

Tuplas são imutáveis!
"""
lanche = ('hamburguer', 'suco', 'pizza', 'pudim')

# laços com a tupla
for word in lanche:
    print(f'O lanche é {word} (com o for in na tupla)')

for cont in range(0, len(lanche)):
    print(f'O lanche é {lanche[cont]} (com o for in de contador)')

for pos, word in enumerate(lanche):
    print(f'O lanche é {word} na posição {pos} (com o for no enumerate)')

print('FIM')

tuplaPessoa = ('Lin', 26, 'M', 82.4)
print(tuplaPessoa)

lanche[2] = 'vai dar erro aqui pois a tupla é imutável'
