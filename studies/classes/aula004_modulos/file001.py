# import [taltal] (importa uma biblioteca inteira)
# from [biblioteca] import [taltal] (importa algo específico de uma biblioteca)
# from [biblioteca] import [taltal],[outro taltal] (importa dois objetos específicos de uma biblioteca)

import math

number = int(input('Digite um número: '))
print('A raiz de {} é igual a {}.'.format(number, math.sqrt(number)))
