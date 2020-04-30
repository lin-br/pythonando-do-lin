"""
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo"
"""
city = input('Digite o nome de uma cidade: ').strip()

print('Ela começa com o nome "Santo" ? -> {}'.format(city.lower().find('santo') == 0))
