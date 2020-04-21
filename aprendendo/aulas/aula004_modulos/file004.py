# import [taltal] (importa uma biblioteca inteira)
# from [biblioteca] import [taltal] (importa algo específico de uma biblioteca)
# from [biblioteca] import [taltal],[outro taltal] (importa dois objetos específicos de uma biblioteca)

from math import sqrt

number = int(input('Digite um número: '))
print('A raiz quadrada de {} é igual a {}.'.format(number, sqrt(number)))
