"""
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre:

A média de idade do grupo.
Qual é o nome do homem mais velho.
Quantas mulheres têm menos de 20 anos.
"""
totalYears = 0
yearManOld = 0
name = ''
totalWoman = 0

for x in range(0, 4):
    nameInput = input('Digite o nome: ').strip()
    yearsInput = int(input('Digite a idade: '))
    genderInput = input('Digite o sexo [M/F: ')
    totalYears += yearsInput
    if genderInput in 'Mm' and yearsInput > yearManOld:
        name = nameInput
        yearManOld = yearsInput
    if genderInput in 'Ff' and yearsInput < 20:
        totalWoman += 1

print('A média da idade do grupo é {}'.format(totalYears // 4))
print('O nome do homem mais velho é {}'.format(name))
print('Quantidade de mulheres com menos de 20 anos é {}'.format(totalWoman))
