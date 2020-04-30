"""
Desenvolva um programa que leia o comprimento de três
retas e diga ao usuário se elas podem ou não formar um triângulo.
"""
retaOne = int(input('Digite o comprimento da primeira reta: '))
retaTwo = int(input('Digite o comprimento da segunda reta: '))
retaThree = int(input('Digite o comprimento da terceira reta: '))

ifOne = (retaOne + retaTwo) > retaThree
ifTwo = (retaTwo + retaThree) > retaOne
ifThree = (retaOne + retaThree) > retaTwo

print('PARABÉNS! É possível formar um triângulo' if (
        ifOne and ifTwo and ifThree) else 'Não é possível formar um triângulo')
