""" 1. O IMC – Índice de Massa Corporal é um critério da Organização Mundial de Saúde
para dar uma indicação sobre a condição de peso de uma pessoa adulta. A fórmula é IMC
= peso / altura2 . Implemente um programa que leia o peso e a altura de um adulto e mostre
sua condição de acordo com a tabela abaixo."""

peso = float(input("Digite o seu peso em Kg: (75.4kg = 75.4) "))
altura = float(input("Digite sua altura em cm: (183cm = 183) "))
imc = peso / (altura * altura)
print(imc)

if imc < 18.5:
    print("Você está abaixo do peso")
elif imc >= 18.5 and imc <= 25:
    print("Você está no seu peso ideal")
elif imc > 25 and imc <= 30:
    print("Você está com sobre do peso")
else:
    print("Você está obeso")
