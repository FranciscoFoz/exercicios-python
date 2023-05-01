# NÚMERO DE REGISTRO - HEXADECIMAL

'''
Crie um programa que pergunte ao usuário se ele deseja converter o número de registro para hexadecimal ou
se ele deseja converter o número hexadecimal em número de registro (um número inteiro).

Em seguida, converta esse número em sua respectiva conversão e imprima na tela.

'''
def int_para_hex():
    numero_registro = int(input("Digite o número de registro do livro: "))
    numero_registro = hex(numero_registro)
    print("O número de chamada do livro é: {}".format(numero_registro))

def hex_para_int():
    numero_registro = input("Digite o número de registro do livro em hexadecimal: ")
    numero_registro = numero_registro.replace('0x','')
    
    def hex_output(hexnum):
        numero = 0
        for potencia, digito in enumerate(reversed(hexnum)):
            numero += int(digito,16) * (16** potencia)
        return numero
    
    numero_registro = hex_output(numero_registro)
    print("O número de chamada do livro é: {}".format(numero_registro))

conversao_desejada = input("Digite '1' para converter o número de registro para hexadecimal \nou '2' para converter o hexadecimal para o número de registro: ")

if conversao_desejada == '1':
    int_para_hex()
elif conversao_desejada == '2':
    hex_para_int()
else:
    print("Opção inválida. Tente novamente.")

