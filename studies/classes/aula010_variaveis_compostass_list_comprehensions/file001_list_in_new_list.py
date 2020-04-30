# list comprehensions in new list

# exemplo 1
ex1 = []
for item in range(10):
    ex1.append(item * 2)

# em uma única linha:
ex1 = [item * 2 for item in range(10)]

# exemplo 2
ex2 = ['a', 'b', 'c']
result = []
for item in ex2:
    result.append(str(item).upper())

# em uma única linha
result = [str(item).upper() for item in ex2]
