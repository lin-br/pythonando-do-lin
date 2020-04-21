"""
Crie um programa que leia quanto dinheiro uma pessoa
tem na carteira e mostre quantos dólares ela pode
comprar.
Considere que US$ 1.00 dólar = R$ 3,27 reais
"""
money = float(input('Valor na sua carteira R$ '))
print('Com o valor de R$ {:.2f} reais, você pode comprar US$ {:.2f} dólares!'.format(money, (money / 3.27)))
