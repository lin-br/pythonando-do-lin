"""
O mesmo professor do desafio anterior quer sortear a ordem de apresentação de
trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
"""
from random import shuffle

studentOne = input('Nome do primeiro aluno: ')
studentTwo = input('Nome do primeiro segundo: ')
studentThree = input('Nome do primeiro terceiro: ')
studentFour = input('Nome do primeiro quarto: ')
deck = [studentOne, studentTwo, studentThree, studentFour]
print('Nomes digitados: {}'.format(deck))
shuffle(deck)
print('Ordem sorteada: {}'.format(deck))
