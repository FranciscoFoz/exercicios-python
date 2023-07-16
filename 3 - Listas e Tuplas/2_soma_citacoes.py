# SOMA CITAÇÕES
'''
Você está desenvolvendo um sistema de contagem de citações em artigos científicos de um períodico 
para analisar a relevância dos trabalhos publicados. 

Você recebe uma lista de valores que representam as citações recebidas por cada artigo.

Cada valor pode ser apenas um número inteiro.

Sua tarefa é implementar uma função que calcule a soma total das citações recebidas por todos os artigos,
considerando o seguinte critério:

Se um valor for um número inteiro, ele deve ser somado diretamente ao total.
Se um valor for uma string representando um número, ele deve ser convertido para inteiro e somado ao total.
Se um valor for uma string representando uma letra, ele deve ser ignorado e uma mensagem de aviso deve ser exibida.
Se um valor for uma lista de números de citação, ele deve ser ignorado e uma mensagem de aviso deve ser exibida.


'''
def soma_citacoes(*itens):
    
    total = 0
    
    for item in itens:
        try:
            
            if isinstance(item, str):
                item = int(item) 
            total += int(item)
        
        except (ValueError):
            print(f'Esse argumento continha uma string com letras e o elemento "{item}" foi ignorado')
            pass
        except (TypeError):
            print(f'Esse argumento continha uma lista e o elemento "{item}" foi ignorado.')
            pass
        
    return itens, total

resultado = soma_citacoes(10, 20, 30,'20','a',[40], 40)

print(f'O total da soma dos elementos: {resultado[0]}\nfoi de {resultado[1]}.')