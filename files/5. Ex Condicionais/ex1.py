'''Tendo como dados de entrada a altura e o sexo de uma pessoa, implemente um
programa que calcule seu peso ideal, utilizando as seguintes fórmulas:
- para homens: (72.7 * h) - 58;
- para mulheres: (62.1 * h) - 44.7'''

print("Seja bem vindo a calculadora do peso ideal!!!")
sexo = input("Digite o seu gênero, Masculino (M) ou Feminino (F): ").lower()
altura = float(input("Digitel sua altura em cm: (183cm = 1.83) "))
imc = 0

if sexo == "m" or sexo == "masculino":
    imc = (72.7 * altura) - 58
    print(f"Seu imc ideal é: {imc:.2f}")
elif sexo == "f" or sexo == "feminino":
    imc = (62.1 * altura) - 44.7
    print(f"Seu imc ideal é: {imc:.2f}")
elif imc == 0:
    print("ERROR!!! Digite um gênero válido!")


