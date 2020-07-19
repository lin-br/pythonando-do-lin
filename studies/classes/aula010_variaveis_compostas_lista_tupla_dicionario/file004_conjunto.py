"""
Variáveis compostas
    Tuplas inicia com ()
    Lista inicia com []
    Dicionário inicia com {}
    Conjuntos inicia com {}

Dicionário são mutáveis
"""

l1 = [1, 1, 2, 3, 4, 5, 5, 5, 6, 6, 7, 8, 8]

# Cria um conjunto, neste caso, vai remover dados repetidos
conjunto = set(l1)
print(conjunto)  # {1,2,3,4,5,6,7,8}

# Cria um conjunto diretamente
conjunto2 = {3, 5, 10, 11, 12}

# diferença entre conjuntos, neste caso do primeiro removendo o segundo
print(conjunto - conjunto2)  # {1,2,4,6,7,8}

# união de conjuntos
print(conjunto | conjunto2)  # {1,2,3,4,5,6,7,8,10,11,12}

# interseção de conjuntos / o que tem de comum
print(conjunto & conjunto2)  # {3,5}

# elementos que não aparecem em ambos ao mesmo tempo
print(conjunto ^ conjunto2)  # {1,2,4,6,7,8,10,11,12}
