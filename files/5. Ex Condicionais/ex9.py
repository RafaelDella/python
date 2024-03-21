"""9. Implementar um programa que valide um CPF. Para tanto, solicitar em separado cada
um dos 11 dígitos do CPF."""

def multiplicar_e_somar(lista):
    lista_inteiros = [int(x) for x in lista]

    if len(lista_inteiros) < numero_digitos_verificacao:
        return f"A lista precisa ter pelo menos {numero_digitos_verificacao} elementos"

    resultado = 0
    for i in range(numero_digitos_verificacao):
        resultado += lista_inteiros[i] * (valor_multiplicacao - i)

    return resultado

def segunda_verificacao():
    return multiplicar_e_somar(cpf[:10])

'''Setup'''
numero_digitos_verificacao = 9
valor_multiplicacao = 10
cpf = input("Digite o seu CPF SEM FORMATAÇÃO: ")
primeiro_digito_verificador = int(str(cpf)[-2])
segundo_digito_verificador = int(str(cpf)[-1])

resto_segundo_digito_verificador = 0
segunda_multiplicação = 0

'''Verificar o Primiero Digito'''
cpf_multiplicado = multiplicar_e_somar(cpf[:9])
divisao_verificador = (cpf_multiplicado * 10)%11
print(f"Dividido: {cpf_multiplicado}")

if divisao_verificador == primeiro_digito_verificador or divisao_verificador == 10:
    numero_digito_verificacao = 10
    valor_multiplicacao = 11
    segunda_multiplicação = segunda_verificacao()
    resto_segundo_digito_verificador = (segunda_multiplicação * 10) % 11
    print(resto_segundo_digito_verificador)
    print(segundo_digito_verificador)
else:
    print("Fake Nattyy")


if resto_segundo_digito_verificador == segundo_digito_verificador or resto_segundo_digito_verificador == 10:
    print("Seu CPF é valido!!")
else:
    print("Seu CPF não é válido")