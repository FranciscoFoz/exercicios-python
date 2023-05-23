# PALAVRA MAIS LONGA
'''
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

'''


texto= '''
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
'''



def palavra_mais_longa(texto):

    return sorted(texto.split(),key=len)[-1]

print(palavra_mais_longa(texto))
