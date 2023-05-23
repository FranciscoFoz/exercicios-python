# CONTAR PALAVRAS
'''
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

'''

def contar_palavra(titulos, palavra):
    contador = 0
    for titulo in titulos:
        palavras = titulo.lower().split()
        contador += palavras.count(palavra.lower())
    return contador

# Exemplo de utilização
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

palavra = "GPT"

resultado = contar_palavra(artigos, palavra)
print(f"A palavra {palavra} aparece {resultado} vezes nos títulos dos livros.")

