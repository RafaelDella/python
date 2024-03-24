""" 1. O IMC – Índice de Massa Corporal é um critério da Organização Mundial de Saúde
para dar uma indicação sobre a condição de peso de uma pessoa adulta. A fórmula é IMC
= peso / altura2 . Implemente um programa que leia o peso e a altura de um adulto e mostre
sua condição de acordo com a tabela abaixo."""

import re

def remover_caracteres(string):
    nova_string = re.sub(r'[^0-9.]', '', string)
    return nova_string

peso = input("Digite o seu peso em Kg: ")
peso = float(remover_caracteres(peso))
altura = input("Digite sua altura em Metros: ")
altura = float(remover_caracteres(altura))
imc = peso / (altura * altura)

if imc < 18.5:
    print("Você está abaixo do peso!")
    print(f"Seu IMC é {imc:2f}")
elif imc >= 18.5 and imc <= 25:
    print("Você está no seu peso ideal!")
    print(f"Seu IMC é {imc:2f}")
elif imc > 25 and imc <= 30:
    print("Você está com sobre do peso!")
    print(f"Seu IMC é {imc:2f}")
else:
    print("Você está obeso!")
    print(f"Seu IMC é {imc:2f}")