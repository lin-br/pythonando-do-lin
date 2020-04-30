try:
    a = 2 / 0
except:
    print('Infelizmente tivemos um probelma :/')
else:  # opcional, se ocorreu tudo bem executa
    print(f'Divisão ocorreu: {a}')
finally:  # opcional, se ocorreu falha ou sucesso
    print('Volte sempre, muito obrigado!')

try:
    a = 2 / 0
except Exception as erro:
    print(f'Problema encontrado foi: {erro.__class__}')
else:  # opcional, se ocorreu tudo bem executa
    print(f'Divisão ocorreu: {a}')
finally:  # opcional, se ocorreu falha ou sucesso
    print('Volte sempre, muito obrigado!')

try:
    a = 2 / 0
except ZeroDivisionError:
    print('Não é possível dividir um número por zero')
else:  # opcional, se ocorreu tudo bem executa
    print(f'Divisão ocorreu: {a}')
finally:  # opcional, se ocorreu falha ou sucesso
    print('Volte sempre, muito obrigado!')

try:
    divisor = int(input('Digite um número: '))
    a = 2 / divisor
except (ValueError, TypeError):
    print('O tipo digitado para a divisão não foi identificado')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero')
except Exception as erro:
    print(f'Um erro foi encontrado: {erro.__cause__}')
else:  # opcional, se ocorreu tudo bem executa
    print(f'Divisão ocorreu: {a}')
finally:  # opcional, se ocorreu falha ou sucesso
    print('Volte sempre, muito obrigado!')
