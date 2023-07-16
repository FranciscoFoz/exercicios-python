# Exercícios

## 1 - Ordenar Títulos
Desafio:

O desafio consiste em ordenar uma lista de títulos de livros em ordem alfabética e deixá-los separados por vírgula.
A lista de títulos é fornecida como uma string chamada "titulos", onde cada título está em uma nova linha.


Segue exemplo de lista:
O Senhor dos Anéis
Harry Potter e a Pedra Filosofal
1984
O Lobo da Estepe
Cem Anos de Solidão
A Metamorfose
A Revolução dos Bichos
Crime e Castigo
Macunaíma

## 2 - Palavra mais longa
Desafio:

O desafio consiste em criar uma função que irá receber um texto (string) e retornará a palavra mais longa.


Segue exemplo de texto:

O Louco do Python

No meu computador,
o Python habita
e com ele eu desvendo
a lógica infinita

Nas linhas de código
encontro o meu ser
e através da sintaxe
posso me conhecer

As funções e métodos
são como os versos
que em harmonia se unem
formando universos

E como Pessoa disse
somos todos um pouco
no Python me encontro
e me torno outro louco

Louco pela programação
e por tudo que ela traz
em um mundo digital
onde a criatividade jaz

Então que o Python
seja minha poesia
e em cada linha de código
eu encontre a sabedoria.

Autoria: CHATGPT

## 3 - CONTAR PALAVRAS

Desafio:

Você trabalha em uma biblioteca e recebeu uma lista de títulos de artigos. 
Sua tarefa é criar um programa que conte quantas vezes uma determinada palavra aparece nos títulos dos artigos. 
Para isso, você deve utilizar o método .split() para separar as palavras em cada título.

artigos = [
'RecurrentGPT: Interactive Generation of (Arbitrarily) Long Text',
'VideoLLM: Modeling Video Sequence with Large Language Models',
'Watermarking Text Data on Large Language Models for Dataset Copyright Protection',
'InheritSumm: A General, Versatile and Compact Summarizer by Distilling from GPT',
'Can Large Language Models emulate an inductive Thematic Analysis of semi-structured interviews? An exploration and provocation on the limits of the approach and the model',
'GPT-SW3: An Autoregressive Language Model for the Nordic Languages',
'The Emergence of Economic Rationality of GPT',
'Can We Edit Factual Knowledge by In-Context Learning?',
'G3Detector: General GPT-Generated Text Detector',
'GPT Paternity Test: GPT Generated Text Detection with GPT Genetic Inheritance'
]

## 4 - PROCESSAR REGISTRO MARC

Desafio:

Escreva um programa que leia o texto fornecido e exiba as seguintes informações:

O título do livro: o campo MARC que começa com "245".
O sobrenome e nome do autor: o campo MARC que começa com "100".
O sobrenome e nome do tradutor: o campo MARC que começa com "700".
O ano de publicação: o campo MARC que começa com "260".
O número de páginas: o campo MARC que começa com "300".

Texto fornecido:

LDR 00000        2200000   4500
001 0123456789
008 210524s2023    xx            000 0 eng d
020 ## $a9780140449136 (paperback)
100 1# $aDostoiévski, Fyodor,$d1821-1881.
245 10$aCrime e Castigo /$cFyodor Dostoiévski ; traduzido por Constance Garnett.
250 ## $aEdição especial.
260 ## $aSão Paulo :$bEditora Exemplo,$c2023.
300 ## $a500 páginas ;$c21 cm.
336 ## $atext$btxt$2rdacontent
337 ## $aunmediated$bn$2rdamedia
338 ## $avolume$bnc$2rdacarrier
500 ## $aInclui notas de rodapé.
520 ## $a"Crime e Castigo" é um dos romances mais influentes da literatura mundial. Ele explora a mente atormentada de Raskólnikov, um jovem estudante que comete um assassinato e lida com as consequências emocionais e morais de seus atos.
650 #0 $aRomance russo.
650 #0 $aAssassinato$xFicção.
700 1# $aGarnett, Constance,$d1861-1946,$etr.
710 2# $aEditora Exemplo.

## 5 - GERAR CÓDIGO ENTRADA 

Desafio:

Escreva um programa que gere um código de entrada de um documento, a partir do seu título, autoria, ano de publicação 
e data/hora de entrada atuais.

O código deverá conter todas as letras em maiúsculas e não deverá conter caracteres especiais e espaços em branco.
O título deverá ser retornado de forma completa.
A autoria deverá ser retornada apenas os 3 primeiros caracteres.

Os quatro elementos do código (título, autoria, ano de publicação e data/hora de chegada) deverão ser separados por "_".

Utilize as bibliotecas datetime e unicodedata.