"""
Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
sabendo que o carro custa R$ 60 reais por dia e R$ 0,15 centavos por Km rodado.
"""
km = float(input('Quilômetros percorridos: '))
days = int(input('Quantidade de dias alugados: '))
print('O veículo ficou alugado por {} dias e percorreu {}km.'.format(days, km), end=' ')
print('O valor total do aluguel ficou: R$ {:.2f} reais'.format(((km * 0.15) + (days * 60))))
