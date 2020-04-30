numberOne = int(input('Digite um valor: '))
numberTwo = int(input('Digite um outro valor: '))

sum = numberOne + numberTwo
mult = numberOne * numberTwo
div = numberOne / numberTwo
divFull = numberOne // numberTwo
pot = numberOne ** numberTwo
restOfDiv = numberOne % numberTwo

print('Os números digitados foram: {} e {}'.format(numberOne, numberTwo))
print('A soma é {}, o produto é {}, a divisão é {:.3f}.'.format(sum, mult, div), end=' ')
print('A divisão inteira é {} e a potência é {}.'.format(divFull, pot), end=' ')
print('O resto da divisão é {}.'.format(restOfDiv))
