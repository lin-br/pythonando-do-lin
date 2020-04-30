"""
Faça um programa que leia o preço de um produto e
mostre seu novo preço com 5% de desconto.
"""
price = float(input('Digite o preço de um produto R$ '))
print('O novo valor do produto é de R$ {:.2f}'.format(price - (price * 0.05)))
