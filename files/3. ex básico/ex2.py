"""Faça um algoritmo que calcule o salário, com desconto de imposto, de um PJ"""
valor_hora = float(input("Digite o valor da sua hora: "))
horas_trabalhadas = float(input("Digite a quantidade das horas trabalhadas: "))
imposto = float(input("Digite a % do imposto a ser descontado (5% = 5): "))
salario = valor_hora * horas_trabalhadas
valor_imposto = (valor_hora * horas_trabalhadas) * (imposto/100)
valor_final = salario - valor_imposto
print(f'O total a recerber é R${valor_final:.2f}')
