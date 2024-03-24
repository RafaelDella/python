"""9. Implementar um programa que valide um CPF. Para tanto, solicitar em separado cada
um dos 11 dígitos do CPF."""

def multiplicar_e_somar(lista):
    lista_cpf = [int(x) for x in lista]

    if len(lista_cpf) < quant_digitos_verificar:
        return f"A lista precisa ter pelo menos {quant_digitos_verificar} elementos"

    resultado = 0
    for i in range(quant_digitos_verificar):
        resultado += lista_cpf[i] * (valor_multiplicacao - i)

    return resultado

def segunda_verificacao():
    return multiplicar_e_somar(cpf[:quant_digitos_verificar])

'''Definindo variável global'''
quant_digitos_verificar = 9
valor_multiplicacao = 10
cpf = input("Digite o seu CPF SEM FORMATAÇÃO: ")
primeiro_digito_verificador = int(str(cpf)[-2])
segundo_digito_verificador = int(str(cpf)[-1])
resto_segundo_digito_verificador = 0
segunda_multiplicação = 0

'''Verificar o Primiero Digito'''
cpf_multiplicado = multiplicar_e_somar(cpf[:9])
resto_divisao_verificador = (cpf_multiplicado * 10)%11

if resto_divisao_verificador == primeiro_digito_verificador or resto_divisao_verificador == 10:
    quant_digitos_verificar = 10
    valor_multiplicacao = 11
    segunda_multiplicação = segunda_verificacao()
    resto_segundo_digito_verificador = (segunda_multiplicação * 10) % 11
else:
    print("Seu CPF não é válido!")


if resto_segundo_digito_verificador == segundo_digito_verificador or resto_segundo_digito_verificador == 10:
    print("Seu CPF é valido!!")
else:
    print("Seu CPF não é válido")