# Empréstimos semana

'''
Desafio:

O desafio consiste em escrever  um programa que receba o número de livros emprestados 
por dia de uma biblioteca ao longo de uma semana (7 dias) e calcule:

* O número total de livros emprestados na semana
* A média diária de empréstimos
* O dia com o maior número de empréstimos

Ao final, exiba os resultados para o usuário.

'''

total_emprestimos = 0
maior_emprestimo = 0
dia_maior_emprestimo = 0

for dia in range(1, 8):
    emprestimo = int(input(f"Digite o número de empréstimos do dia {dia}: "))
    total_emprestimos += emprestimo
    
    if emprestimo > maior_emprestimo:
        maior_emprestimo = emprestimo
        dia_maior_emprestimo = dia

quantidade_dias = 7
media_diaria = round((total_emprestimos / quantidade_dias))

print(20*'-')
print(f"Total de empréstimos na semana: {total_emprestimos}")
print(f"Média diária de empréstimos: {media_diaria:.2f}")
print(f"Dia com maior número de empréstimos: {dia_maior_emprestimo}")
print(20*'-')