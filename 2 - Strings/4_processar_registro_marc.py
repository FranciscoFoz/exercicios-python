# PROCESSAR REGISTRO MARC
'''
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


'''

registro_marc = '''LDR 00000        2200000   4500
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
'''


def processar_registro_marc(texto):
    titulo_inicio = texto.find("245 10$a") + len("245 10$a")
    titulo_fim = texto.find("/$c", titulo_inicio)
    titulo = texto[titulo_inicio:titulo_fim]

    autor_inicio = texto.find("100 1# $a") + len("100 1# $a")
    autor_fim = texto.find(",$d", autor_inicio)
    autor = texto[autor_inicio:autor_fim]
    
    tradutor_inicio = texto.find("700 1# $a") + len("700 1# $a")
    tradutor_fim = texto.find(",$d", tradutor_inicio)
    tradutor = texto[tradutor_inicio:tradutor_fim]

    ano_inicio = texto.find("260 ## $aSão Paulo :$bEditora Exemplo,$c") + len("260 ## $aSão Paulo :$bEditora Exemplo,$c")
    ano_fim = ano_inicio + 4
    ano = texto[ano_inicio:ano_fim]

    paginas_inicio = texto.find("300 ## $a") + len("300 ## $a")
    paginas_fim = texto.find(" páginas", paginas_inicio)
    paginas = texto[paginas_inicio:paginas_fim]
        

    return titulo, autor, tradutor, ano, paginas

registro_marc_processado = processar_registro_marc(registro_marc)

print(f'''
      Título: {registro_marc_processado[0]}
      Autor: {registro_marc_processado[1]}
      Tradutor: {registro_marc_processado[2]}
      Ano: {registro_marc_processado[3]}
      Páginas: {registro_marc_processado[4]}''')
