# list comprehensions with if

# exemplo 1
result = []
for number in range(20):
    if number % 2 == 0:
        result.append(number)

# em uma única linha
result = [number for number in range(20) if number % 2 == 0]
