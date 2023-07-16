# BUSCAR DOCUMENTOS
'''
Desafio:

O desafio consiste em criar uma função que recebe uma lista de palavras-chave e 
uma quantidade variável de documentos como argumentos (*args). 

A função deve retornar uma lista de documentos que contenham todas as palavras-chave fornecidas.

Segue exemplo de lista:

livros_biblioteconomia = [
    "Introdução às Ciências da Documentação",
    "Fundamentos da Biblioteconomia e Ciência da Informação",
    "Catalogação: conceitos e práticas",
    "Organização de Bibliotecas Digitais",
    "Arquitetura da Informação: fundamentos, métodos e aplicações",
    "Administração de Bibliotecas",
    "Preservação e Conservação de Documentos e Obras de Arte",
    "Bibliotecas Digitais: conceitos e práticas",
    "Avaliação de Serviços de Informação",
    "Marketing de Serviços de Informação"
]

Segue exemplo de palavras-chave: 

palavras_chave = ["informação"]

'''

def buscar_documentos(palavras_chave, *documentos):
    documentos_encontrados = []
    for documento in documentos:
        palavras_documento = documento.lower().split()
        
        if all(palavra.lower() in palavras_documento for palavra in palavras_chave):
            documentos_encontrados.append(documento)
    
    return documentos_encontrados

livros_biblioteconomia = [
    "Introdução às Ciências da Documentação",
    "Fundamentos da Biblioteconomia e Ciência da Informação",
    "Catalogação: conceitos e práticas",
    "Organização de Bibliotecas Digitais",
    "Arquitetura da Informação: fundamentos, métodos e aplicações",
    "Administração de Bibliotecas",
    "Preservação e Conservação de Documentos e Obras de Arte",
    "Bibliotecas Digitais: conceitos e práticas",
    "Avaliação de Serviços de Informação",
    "Marketing de Serviços de Informação"
]


palavras_chave = ["informação"]

resultados = buscar_documentos(palavras_chave, *livros_biblioteconomia)

for i,titulo in enumerate(resultados):
    print(f'{i+1} - {titulo}')
