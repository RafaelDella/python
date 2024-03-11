"""Crie um algoritmo que calcule o IMC do usuário"""
peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em metros: "))
imc = peso/(altura*altura)
print(f"O seu IMC é de: {imc:.2f}")
