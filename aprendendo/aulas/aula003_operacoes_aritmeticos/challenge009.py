"""
Faça um programa que leia o salário de um funcionário e mostre
seu novo salário com 15% de aumento.
"""
salary = float(input('Digite o salário R$ '))
print('O novo salário é R$ {:.3f}'.format(salary + (salary * 0.15)))
