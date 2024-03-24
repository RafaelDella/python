'''6. Implemente um programa para calcular as raízes de uma equação do 2º grau, sendo que
os valores dos coeficientes A, B, e C devem ser fornecidos pelo usuário, e os valores das
raízes devem ser calculadas pela fórmula de Bhaskara, como segue'''

import math

a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))
delta = ((b*b) - (4*a*c))

if delta < 0:
    print(f"Não existe raizes de números reais para o valor de {delta:.2f}")
else:
    x1 = (-1 * (b) + math.sqrt(delta))/(2*a)
    x2 = (-1 * (b) - math.sqrt(delta))/(2*a)
    print(f"O valor de X1 é {x1}")
    print(f"O valor de X2 é {x2}")