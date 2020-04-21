# import [taltal] (importa uma biblioteca inteira)
# from [biblioteca] import [taltal] (importa algo específico de uma biblioteca)
# from [biblioteca] import [taltal],[outro taltal] (importa dois objetos específicos de uma biblioteca)

import math

number = int(input('Digite um número: '))
sqrt = math.sqrt(number)
print('A raiz quadrada ARREDONDADA PARA BAIXO de {} é igual a {}.'.format(number, math.floor(sqrt)))
