# Ordenação de Artigos 
'''

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
'''
from datetime import datetime, date

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

def calcular_media_consultas(artigo):
    data_publicacao = datetime.strptime(artigo['data_publicacao'], '%d/%m/%Y').date()
    dias_desde_publicacao = (date.today() - data_publicacao).days
    media_consultas = artigo['consultas'] / dias_desde_publicacao if dias_desde_publicacao > 0 else 0
    return round(media_consultas, 2)


def ordenar_por_data(artigos):
    artigos.sort(key=lambda artigo: datetime.strptime(artigo['data_publicacao'], '%d/%m/%Y'))
    return artigos

artigos_ordenados = ordenar_por_data(artigos)

for artigo in artigos_ordenados:
    ano_publicacao = datetime.strptime(artigo['data_publicacao'], '%d/%m/%Y').year
    media_consultas = calcular_media_consultas(artigo)
    print(10*'-')
    print(f"{artigo['titulo']} ({ano_publicacao}) \n- {artigo['consultas']} consultas \n- Média de {media_consultas} consultas por dia")


