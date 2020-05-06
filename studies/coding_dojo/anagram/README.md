# Problem Description

## Completed tasks
- [ ] 1st task
- [ ] 2nd task
- [ ] 3rd task
- [ ] 4th task

## Your tasks
### 1st task
Escreva um programa que gere todos os anagramas de duas palavras da string "documenting" com
a lista de palavras que consta no arquivo `wordlist.txt`.

### 2nd task
Escreva um progama que calcule a quantidade possível de anagramas de uma determina palavra,
sentença ou frase.

### 3rd task
Agora desenvolva um algoritmo que encontre um determinado anagrama dentro de uma frase
ou sentença.

### 4th task
Implemente concurrencia a busca e comparação da primeira tarefa.

## Anagrama
Para começar, vamos primeiro identificar o que o Kata está pedindo.

**O que é um anagrama?**
Um anagrama é a permutação entre as letras de uma palavra, os números de uma sequência ou os elementos
de um conjunto qualquer. Então, os cálculos que envolvem anagramas geralmente terão o objetivo
de descobrir de quantas formas é possível reordenar os elementos de um conjunto no qual a ordem desses
elementos tem relevância.

**Exemplo**: de quantas maneiras é possível escolher a senha para um cartão de crédito sabendo-se
que podem ser escolhidos quatro números de 0 a 9 sem que eles se repitam?

**O que é permutação?**
É a troca de lugar entre dois ou mais elementos de um conjunto ordenado. Como um anagrama é uma nova
palavra ou lista obtida por meio dos elementos de outra palavra ou lista, o anagrama é obtido com uma
permutação.

**Exemplo de anagrama**:
* O conjunto de letras OVA possui os seguintes anagramas:
OVA, OAV, VOA, VAO, AOV e AVO
* Alguns anagramas da palavra PATO:
PATO, TOPA E OPTA

### Cálculo de permutação
O cálculo da permutação de um conjunto é realizado da seguinte fórmula:
```text
P = n!
```
Sendo `n!` calculado da seguinte maneira:
```text
n! = n*(n-1)*(n-2)*(n-3)*(n-4)...
```
Exemplo:
```text
P = 4! -> P = 4*3*2*1 -> P = 24
```

### Cáluclo de anagrama
O cálculo de anagrama utiliza o cálculo da permutação de um conjunto menos ele mesmo.
Exemplo da palavra TOPA:
```text
A palavra TOPA é formada por 4 letras, sendo assim, 4 espaços: 4! -> 4*3*2*1 = 24
```
A palavra TOPA possui um total de 23 anagramas, permutação de 4 menos 1, ou 24 - 1.

No caso de uma palavra que possua letras iguais, nós precisamos seguir a seguinte fórmula:
````text
Pn(n1,n2,n3...) = n!/n1!*n2!*n3!...
````
* Exemplo com a palavra CASA, ela é formada por 4 letras, mas a letra A é repetida 2 vezes:
````text
P4(2) -> P4(2) = 4!/2! -> P4(2) = 24/2 -> P4(2) = 12
````
Neste caso, a palavra CASA possui 11 anagramas (12 - 1).

* Exemplo com a palavra ABACAXI, ela é formada por 7 letras, mas a letra A é repetida 3 vezes:
````text
P7(3) -> P7(3) = 7!/3! -> P7(3) = 5040/6 -> P7(3) = 840
````
Neste caso, a palavra ABACAXI possui 840 anagramas.

* Exemplo com a palavra VITAMINA, ela é formada por 8 letras, mas possui a letra I
e a letra A repetidas 2 vezes cada uma.
````text
P8(2,2) -> P8(2,2) = 8!/2!*2! -> P8(2,2) = 40320/4 -> P8(2,2) = 10080
````
Neste caso, a palavra VITAMINA possui 10080 anagramas.
