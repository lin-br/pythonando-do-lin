# list comprehensions with more if

# exemplo 1
result = []
for number in range(100):
    if number % 5 == 0:
        result.append('1')
    else:
        result.append('0')

# em uma única linha
result = ['1' if number % 5 == 0 else '0' for number in range(16)]
