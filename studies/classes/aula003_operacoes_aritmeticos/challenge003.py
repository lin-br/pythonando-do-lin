"""
Desenvolva um programa que leia as duas notas de um aluno,
calcule e mostre a sua média.
"""
scoreOne = float(input('Digite a sua primeira nota: '))
scoreTwo = float(input('Digite a sua segunda nota: '))
print('A média da sua nota é {:.1f}.'.format((scoreOne + scoreTwo) / 2).format())
