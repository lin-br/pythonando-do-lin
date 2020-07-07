# Desafios

## University :white_check_mark: [Resultado](https://github.com/lin-br/pythonando-do-lin/tree/master/studies/idtrust/university)
A Universidade iDtrust tem as seguintes regras para as notas dos seus alunos:
* Cada aluno pode ter notas que vão entre 0 e 100, inclusive.
* Cada nota menor que 40 é considerado como reprova.
A Universidade arredonda as notas dos seus alunos de acordo com as seguintes regras:
* Se a diferença entre a nota e o próximo múltiplo de 5 for menor que 3, arredonda a nota para o próximo múltiplo de 5.
* Se a nota é menor que 38, não ocorre arredondamento pois o resultado ainda seria uma nota de reprovação.
Por exemplo, uma nota igual a 84 seria arredondada para 85 mas uma nota igual a 29 não seria arredondada
porque o resultado seria uma nota menor que 40.
Dado o valor inicial da nota para cada n alunos, escreva um algoritmo que automatize o arredondamento das
notas de acordo com as regras acima e imprima o valor do resultado em uma nova linha.
### Input format
A primeira linha representa **n**, o número de alunos. Cada linha **i** das **n** linhas seguintes contém um inteiro que
representa a nota de um aluno (**ni**).
### Limitations
* 1 ≤ n ≤ 60
* 0 ≤ nota ≤ 100
### Output format
Para cada nota das **n** notas, imprima a nota arredondada em uma nova linha.
### Input example:
```text
4
73
67
38
33
```
### Output example:
```text
75
67
40
33
```
## Challenge FIFO :white_check_mark: [Resultado](https://github.com/lin-br/pythonando-do-lin/tree/master/studies/idtrust/challenge_fifo)
Uma fila é um tipo abstrato de dados que mantém a ordem que os elementos são inseridos, permitindo que os
elementos mais antigos sejam removidos do início e novos elementos sejam adicionados no fim.
Essa estrutura de dados é chamada de **FIFO (first-in-first-out)** pois o primeiro elemento adicionado
à fila é sempre o primeiro a ser removido. Uma fila básica tem as seguintes possíveis operações:
* Enfileirar: Adiciona um elemento no final da fila.
* Desenfileirar: Remove o elemento do início da fila e retorna o mesmo.

Nesse exercício você deve implementar uma fila utilizando **duas pilhas**. Em seguida, processar **q** operações,
onde cada entrada é de um dos três tipos a seguir:
* **1 x**: Enfilera o elemento x no fim da fila.
* **2**: Desenfileira o elemento do início da fila.
* **3**: Imprime o elemento do início da fila.
### Input format
A primeira linha é um inteiro, **q**, que representa o número de operações. Cada linha **i** das q operações
subsequentes representa uma única operação no formato descrito na lista acima. Todas os três tipos de
operação começam com um inteiro representando o tipo da operação mas somente a primeira operação é seguida
de um espaço e um valor **x** que representa o valor a ser enfileirado.
### Limitations
* 1 ≤ q ≤ 100000
* 1 ≤ tipo ≤ 3
* 1 ≤ |x| ≤ 1000000000
* É garantido que sempre existe um valor válido para cada operação do tipo 3.
### Output format
Para cada operação do **tipo 3**, imprimir o valor do elemento no início da fila em uma nova linha.
### Input example:
```text
10
1 42
2
1 14
3
1 28
3
1 60
1 78
2
2
```
### Output example:
```text
14
14
```