"""
Variáveis compostas
    Tuplas inicia com ()
    Lista inicia com []
    Dicionário inicia com {}
    Conjuntos inicia com {}

Dicionário são mutáveis
"""

dados = dict()
dados['nome'] = 'Lin'
dados['idade'] = 26
dados['sexo'] = 'M'
print(dados)

dados = {'nome': 'Pedro', 'idade': 25}
print(dados)
print(dados['nome'])

dados['sexo'] = 'M'
del dados['idade']
print(dados)

filmes = {
    'titulo': 'Star Wars',
    'ano': 1977,
    'diretor': 'George Lucas'
}
print(filmes.values())  # só os valores
print(filmes.keys())  # só as chaves
print(filmes.items())  # tanto as chaves quanto os valores

# com um for de exemplo:
for key, value in filmes.items():
    print(f'O {key} é {value}')

locadora = list()
locadora.append(filmes)
print(locadora)

# atualiza o dicionário atual com outro
dados.update(filmes)
print(dados)
