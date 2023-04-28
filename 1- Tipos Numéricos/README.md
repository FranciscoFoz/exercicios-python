# Exercícios

## 1 - Valor da multa
Desafio:

O desafio consiste em criar um programa em Python para calcular a multa a ser paga
por um usuário de biblioteca que devolveu um livro com atraso.

Para isso, o programa deve solicitar ao usuário o número de dias que o livro foi devolvido após 
a data de vencimento e calcular a multa com base na seguinte tabela:

* Até 3 dias de atraso: multa de R$ 0,50 por dia de atraso
* De 4 a 7 dias de atraso: multa de R$ 1,00 por dia de atraso
* Mais de 7 dias de atraso: multa de R$ 2,00 por dia de atraso

Ao final, o programa deve exibir a mensagem "O valor da sua multa é R$ X", em que X é o valor da multa calculada.

## 2 - Emprestimos semana
Desafio:

O desafio consiste em escrever  um programa que receba o número de livros emprestados 
por dia de uma biblioteca ao longo de uma semana (7 dias) e calcule:

* O número total de livros emprestados na semana
* A média diária de empréstimos
* O dia com o maior número de empréstimos

Para isso, utilize os seguintes elementos:

Ao final, exiba os resultados para o usuário.

## 3 - Porcentagem de leitura
Desafio:

Crie um programa que solicite ao usuário que digite o número total de páginas
de um livro e o número de páginas que foram lidas, e em seguida,
calcule e imprima a porcentagem do livro que foi lida até o momento.

Caso o usuário insira um número errado de páginas lidas (maior do que o número de páginas do livro),
o programa deve continuar pedindo o número de páginas lidas até que o usuário
indique que terminou de ler o livro, ou seja, tenha lido todas as páginas.

Para realizar essa divisão com precisão exata, utilize o módulo Decimal da biblioteca padrão do Python.

## 4 - Ordenação de artigos
Desafio:

Dada a lista de artigos:

artigos = [
    {'titulo': 'Applications of Artificial Intelligence in Academic Libraries', 
     'autores': ['Vijayakumar, S.','Sheshadri,K.N.'],
     'data_publicacao': '16/05/2019', 
     'consultas': 569},
    {'titulo': 'Data science in data librarianship: Core competencies of a data librarian',
     'autores': ['Semeler, A. R.','Pinto, A. L.','Rozados, H. B. F.'],
     'data_publicacao': '26/11/2019',
     'consultas': 1004},
    {'titulo': 'Data scientist: the sexiest job of the 21st century', 
     'autores': ['Davenport,T.H.','Patil, D J'], 
     'data_publicacao': '01/10/2012', 
     'consultas': 10231},
    {'titulo': 'Bibliometria: evolução histórica e questões atuais',
     'autores': ['Araújo,C.A.A.'],
     'data_publicacao': '10/12/2006',
     'consultas': 650}
]

Crie uma função para ordenar a lista de artigos por data de publicação, do mais antigo ao mais recente.
Utilize as funções sort(), len() e a biblioteca datetime para completar o desafio.

## 5 - Número de registro Hexadecimal
Desafio:

Crie um programa que pergunte ao usuário se ele deseja converter o número de registro para hexadecimal ou
se ele deseja converter o número hexadecimal em número de registro (um número inteiro).

Em seguida, converta esse número em sua respectiva conversão e imprima na tela.