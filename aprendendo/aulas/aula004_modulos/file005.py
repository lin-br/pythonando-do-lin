# import [taltal] (importa uma biblioteca inteira)
# from [biblioteca] import [taltal] (importa algo específico de uma biblioteca)
# from [biblioteca] import [taltal],[outro taltal] (importa dois objetos específicos de uma biblioteca)

from math import sqrt, floor

number = int(input('Digite um número: '))
print('A raiz quadrada ARREDONDADA PARA BAIXO de {} é igual a {}.'.format(number, floor(sqrt(number))))
