"""
Um professor quer sortear um dos seus quatros alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo o nome do escolhido.
"""
from random import choice

studentOne = input('Nome do primeiro aluno: ')
studentTwo = input('Nome do primeiro segundo: ')
studentThree = input('Nome do primeiro terceiro: ')
studentFour = input('Nome do primeiro quarto: ')

print('O aluno que vai apagar o quadro é: {}'.format(choice([studentOne, studentTwo, studentThree, studentFour])))
