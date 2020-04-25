# Problem Description

## User Story 1
Você trabalha em um banco que comprou recentemente uma máquina engenhosa para ajudar na leitura de cartas
e fax enviados pelas filiais. A máquina digitaliza os documentos em papel e produz um arquivo com várias
entradas, cada uma com a seguinte aparência:
```text
    _  _     _  _  _  _  _ 
  | _| _||_||_ |_   ||_||_|
  ||_  _|  | _||_|  ||_| _|
                           
```
Cada entrada tem 4 linhas e cada linha possui 27 caracteres. As três primeiras linhas de cada entrada
contêm um número de conta gravado usando tubos e sublinhados, e a quarta linha está em branco.
Cada número de conta deve ter 9 dígitos, todos no intervalo de 0 a 9. Um arquivo normal contém cerca de 500 entradas.

## User Story 2
Após a primeira _feature_ ser implementada, você percebe que a máquina engenhosa, não é infalível.
Ela falha na validação do número da conta, portanto a próxima etapa é validar se o número da conta
lido é de fato um número de conta válido. Essa verificação possui uma soma que é cálculo da seguinte
maneira:
```text
número da conta:  3  4  5  8  8  2  8  6  5
nome da posição:  d9 d8 d7 d6 d5 d4 d3 d2 d1

cálculo: (d1+2*d2+3*d3+4*d4...+9*d9) mod 11 = 0
```

# Tasks
1. Sua primeira tarefa é escrever um programa que possa pegar esse arquivo e analisá-lo em números de contas reais.
2. Sua segunda tarefa é validar o número da conta lido através do cálculo apresentado no User Story 2.

# Suggested Test Cases
```text
use case 1
 _  _  _  _  _  _  _  _  _ 
| || || || || || || || || |
|_||_||_||_||_||_||_||_||_|

=> 000000000

  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |

=> 111111111
 _  _  _  _  _  _  _  _  _ 
 _| _| _| _| _| _| _| _| _|
|_ |_ |_ |_ |_ |_ |_ |_ |_ 

=> 222222222
 _  _  _  _  _  _  _  _  _ 
 _| _| _| _| _| _| _| _| _|
 _| _| _| _| _| _| _| _| _|

=> 333333333

|_||_||_||_||_||_||_||_||_|
  |  |  |  |  |  |  |  |  |

=> 444444444
 _  _  _  _  _  _  _  _  _ 
|_ |_ |_ |_ |_ |_ |_ |_ |_ 
 _| _| _| _| _| _| _| _| _|

=> 555555555
 _  _  _  _  _  _  _  _  _ 
|_ |_ |_ |_ |_ |_ |_ |_ |_ 
|_||_||_||_||_||_||_||_||_|

=> 666666666
 _  _  _  _  _  _  _  _  _ 
  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |

=> 777777777
 _  _  _  _  _  _  _  _  _ 
|_||_||_||_||_||_||_||_||_|
|_||_||_||_||_||_||_||_||_|

=> 888888888
 _  _  _  _  _  _  _  _  _ 
|_||_||_||_||_||_||_||_||_|
 _| _| _| _| _| _| _| _| _|

=> 999999999
    _  _     _  _  _  _  _ 
  | _| _||_||_ |_   ||_||_|
  ||_  _|  | _||_|  ||_| _|

=> 123456789

use case 2

Input -> This number 457508000 is valid?
Output -> True
```