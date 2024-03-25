"""
7. Implemente um programa que solicite o dia, mês e ano (com 4 dígitos) de nascimento
de uma pessoa, e pergunte em qual formato deve exibir a data, como segue:
"""

def verificar_ano(data):
    while not data.isdigit():
        print("ERROR!! A string não contem apenas números INTEIROS")
        data = input("Digite uma data válida: ")
    
    if verificar_mes == True:
        while int(data) > 12:
            print("ERROR!! A string não contem apenas números INTEIROS")
            data = int(input("Digite um mês válida: "))

    if verificar_dia == True:
        while int(data) > 30:
            print("ERROR!! A string não contem apenas números INTEIROS")
            data = int(input("Digite um dia válida: "))
            verificar_dia == False

    if data != 0:
        if len(data) < quantidade_digito_data:
            data = data.zfill(quantidade_digito_data)
            return data
        elif len(data) > quantidade_digito_data:
            print("ERROR!! Digite uma data VÁLIDO!")
        else:
            return data

quantidade_digito_data = 4
verificar_mes = False
verificar_dia = False
ano = input("Digite um ano: ")
ano = verificar_ano(ano)

quantidade_digito_data = 2
mes = input("Digite um mês: ")
verificar_mes = True
verificar_dia = False
mes = verificar_ano(mes)


dia = input("Digite um dia: ")
verificar_mes = False
verificar_dia = True
dia = verificar_ano(dia)

print("1 – Data simples. Ex.: 10/08/1990")
print("2 – Data abreviada. Ex.: 10/ago/1990")
print("3 – Data completa. Ex.: 10 de agosto de 1990.")
formato = int(input("Qual formato você quer sua data? "))

match formato:
    case 1:
        print("Data Simples!!!")
        print(f"{dia}/{mes}/{ano}")
    case 2:
        match mes:
            case "01":
                mes = "jan"
            case "02":
                mes = "fev"
            case "03":
                mes = "mar"
            case "04":
                mes = "abr"
            case "05":
                mes = "maio"
            case "06":
                mes = "jun"
            case "07":
                mes = "jul"
            case "08":
                mes = "ago"
            case "09":
                mes = "set"
            case "10":
                mes = "out"
            case "11":
                mes = "nov"
            case "12":
                mes = "dez"
        print("Data Abreviada!!!")
        print(f"{dia}/{mes}/{ano}")
    case 3:
        match mes:
            case "01":
                mes = "janeiro"
            case "02":
                mes = "feveveiro"
            case "03":
                mes = "março"
            case "04":
                mes = "abril"
            case "05":
                mes = "maio"
            case "06":
                mes = "junho"
            case "07":
                mes = "julho"
            case "08":
                mes = "agosto"
            case "09":
                mes = "setembro"
            case "10":
                mes = "outubro"
            case "11":
                mes = "novembro"
            case "12":
                mes = "dezembro"
        print("Data Completa!!!")
        print(f"{dia} de {mes} de {ano}")
    case other:
        print("Opção inválida!")
