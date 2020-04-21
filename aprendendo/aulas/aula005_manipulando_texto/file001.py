frase = 'Curso em Video Python'

# Cortando a string e exibindo apenas a parte "P"
print(frase[15])

# Cortando a string e exibindo do "V" até o final de 2 em 2 caracteres
print(frase[9::2])

# Cortando a string e exibindo de 3 em 3 caracteres
print(frase[::3])

# Cortando a parte "Video Python" da string
print(frase[9:])

# Cortando a parte "Curso" da string
print(frase[:5])

# Tamanho da string
print(len(frase))

# Contar quantas vezes o caracter "o" aparece na string
print(frase.count('o'))

# Contar quantas vezes o caracter "o" aparece na parte do 0 até 13
print(frase.count('o', 0, 13))

# Procura a primeira vez que aparece a parte "deo" e mostra o campo dentro da string
print(frase.find("deo"))

# Procura uma parte que não existe dentro da string, retorna o valor -1
print(frase.find("Lin"))

# Infoma se existe uma parte dentro da string, retorna True ou False
print('Py' in frase)

# Trocar uma parte por outra dentro da string
print(frase.replace('Python', 'Android'))

# Transformar todos os caracteres em maiusculos
print(frase.upper())

# Transformar todos os caracteres em minusculo
print(frase.lower())

# Transformar todos os caracteres em minusculo e deixa apenas o primeiro caractere da string em maiusculo
print(frase.capitalize())

# Transformar todos os caracteres em minusculo e deixa apenas o primeiro caractere de cada palavra em maiusculo
print(frase.title())

frase = '   Aprenda Python  '

# Remover os espaços do ínicio e final da string
print(frase.strip())

# Remover os espaços do final (right) da string
print(frase.rstrip())

# Remover os espaços do ínicio (left) da string
print(frase.lstrip())

frase = 'Curso em Video Python'

# Quebrar a string, por padrão é realizado por espaços
print(frase.split())

# Juntar a lista de string com um traço "-"
print('-'.join(frase.split()))
