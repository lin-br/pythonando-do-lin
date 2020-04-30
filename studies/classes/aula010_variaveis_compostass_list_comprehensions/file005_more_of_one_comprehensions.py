# list comprehensions with one matrix

# exemplo 1
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

transposed = []
for i in range(len(matrix[0])):
    line_transposed = []

    for line in matrix:
        line_transposed.append(line[i])
    transposed.append(line_transposed)

# em uma linha
transposed = [[line[i] for line in matrix] for i in range(4)]
"""
1. No primeiro loop, i assume o valor de 0, portanto [linha[0] for linha in matriz]
vai retornar o primeiro elemento de cada linha: [1, 4, 9]
2. No segundo loop, i assume o valor de 1, portanto [linha[1] for linha in matriz]
vai retornar o segundo elemento de cada linha: [2, 5, 10]
3. No terceiro loop, i assume o valor de 2, portanto [linha[2] for linha in matriz]
vai retornar o terceiro elemento de cada linha: [3, 6, 11]
4. No quarto loop, i assume o valor de 3, portanto [linha[3] for linha in matriz]
vai retornar o quarto elemento de cada linha: [4, 8, 12]
"""

# exemplo 2
result = []
for x in [10, 30, 50]:
    for y in [20, 40, 60]:
        result.append(x + y)

# em uma linha
result = [x + y for x in [10, 30, 50] for y in [20, 40, 60]]
