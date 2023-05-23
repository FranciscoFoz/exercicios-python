# ORDENAR TITULOS
'''
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

'''


titulos = """O Senhor dos Anéis
Harry Potter e a Pedra Filosofal
1984
O Lobo da Estepe
Cem Anos de Solidão
A Metamorfose
A Revolução dos Bichos
Crime e Castigo
Macunaíma"""

def ordenar_titulos(titulos):

    titulos_ordenados = sorted(titulos.split("\n"))

    titulos_concatenados = ', '.join(titulos_ordenados)

    return titulos_concatenados


titulos_ordenados = ordenar_titulos(titulos)
print("Títulos ordenados: " + titulos_ordenados)

