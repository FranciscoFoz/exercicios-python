#PORCENTAGEM DE LEITURA
'''
Crie um programa que solicite ao usuário que digite o número total de páginas
de um livro e o número de páginas que foram lidas, e em seguida,
calcule e imprima a porcentagem do livro que foi lida até o momento.

Caso o usuário insira um número errado de páginas lidas (maior do que o número de páginas do livro),
o programa deve continuar pedindo o número de páginas lidas até que o usuário
indique que terminou de ler o livro, ou seja, tenha lido todas as páginas.

Para realizar essa divisão com precisão exata, utilize o módulo Decimal da biblioteca padrão do Python.
'''

from decimal import Decimal

num_paginas_livro = Decimal(input("Digite o número total de páginas do livro: "))
num_paginas_lidas = Decimal(input("Digite o número de páginas que foram lidas: "))

while num_paginas_lidas > num_paginas_livro:
    print('Digite um número válido')
    num_paginas_lidas = Decimal(input("Digite o número de páginas que foram lidas: "))

if num_paginas_lidas == num_paginas_livro:
    print("Você terminou de ler o livro!")
else:
    porcentagem_lida = (num_paginas_lidas / num_paginas_livro) * 100
    print("Porcentagem do livro lida: {:.2f}%".format(porcentagem_lida))




