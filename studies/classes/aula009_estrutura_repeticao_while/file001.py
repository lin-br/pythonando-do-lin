c = 1
while c < 10:
    print(c)
    c += 1
print('FIM')

x = 1
while x != 0:
    x = int(input('Digite um valor: '))
print('FIM')

while True:
    number = int(input('Digite um valor: '))
    if number == 0:
        break
print('FIM')

c = 1
while c < 10:
    print(c)
    c += 1
else:  # comando opcional, executa apenas se o for executar normalmente sem a utilização do break.
    print('FIM')
