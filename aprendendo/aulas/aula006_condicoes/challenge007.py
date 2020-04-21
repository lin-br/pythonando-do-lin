"""
Escreva um programa que pergunte o salário de um funcionário e calcule
o valor do seu aumento.
Para salários superiores a R$ 1250,00, calcule um aumento de 10%.
Para os inferiores ou igual, o aumento é de 15%.
"""
salary = float(input('Digite o salário do funcionário R$ '))
plus = 10 if (salary > 1250) else 15
print('O aumento para esse funcionário deve ser de {}%'.format(plus))
