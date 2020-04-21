name = input('Qual é o seu nome? ')
if name == 'Wesley':
    print('Que nome lindo você tem!')
else:
    print('Que nome comum...')
print('Bom dia, {}!'.format(name))

# ou

print('Que nome lindo você tem!' if name == 'Wesley' else 'Que nome comum...')
