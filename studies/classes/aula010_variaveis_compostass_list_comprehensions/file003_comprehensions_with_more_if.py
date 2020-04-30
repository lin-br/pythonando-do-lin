# list comprehensions with more if

# exemplo 1
result = []
for number in range(100):
    if number % 5 == 0:
        result.append(number)
    if number % 6 == 0:
        result.append(number)

# em uma única linha
result = [number for number in range(100) if number % 5 == 0 if number % 6 == 0]
