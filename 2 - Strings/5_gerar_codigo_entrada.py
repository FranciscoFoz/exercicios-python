# GERAR CÓDIGO ENTRADA 
'''
Desafio:

Escreva um programa que gere um código de entrada de um documento, a partir do seu título, autoria, ano de publicação 
e data/hora de entrada atuais.

O código deverá conter todas as letras em maiúsculas e não deverá conter caracteres especiais e espaços em branco.
O título deverá ser retornado de forma completa.
A autoria deverá ser retornada apenas os 3 primeiros caracteres.

Os quatro elementos do código (título, autoria, ano de publicação e data/hora de chegada) deverão ser separados por "_".

Utilize as bibliotecas datetime e unicodedata.
'''
from datetime import datetime
import unicodedata


def remover_acentos(texto):
    texto = unicodedata.normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII')
    return texto

def gerar_codigo_entrada(titulo, autor, ano_publicacao):
    
    #Tratamento inicial no título
    titulo = remover_acentos(titulo)
    titulo = titulo.strip().upper().replace(" ", "")

    # Remover caracteres especiais
    tabela_caracteres_especiais = str.maketrans("", "", '''!"#$%&'()*+-,./:;<=>?@[\]^_`{|}~''')
    titulo = titulo.translate(tabela_caracteres_especiais)

    #Tratamento inicial no Autor(a)
    autor = remover_acentos(autor).upper()
    autor = autor.translate(tabela_caracteres_especiais)
    
    # Obter a data e hora atual
    data_hora_chegada = datetime.now().strftime("%Y%m%d%H%M%S")

    # Gerar código completo de catalogação
    codigo_completo = f"{titulo}_{autor[:3]}_{ano_publicacao}_{data_hora_chegada}"

    return codigo_completo


# Entrada do usuário
titulo = input("Digite o título do documento: ")
autor = input("Digite o nome do autor(a): ")
ano_publicacao = input("Digite o ano de publicação: ")

# Gerar código de catalogação
codigo_catalogacao = gerar_codigo_entrada(titulo, autor, ano_publicacao)

# Imprimir o código de catalogação
print("Código de entrada:", codigo_catalogacao)
print(unicodedata.normalize('NFKD', 'AZALEÍA').encode('ASCII', 'ignore').decode('ASCII'))
