"""Elaborar um algoritmo que solicita ao usuário o nome de uma disciplina e suas 4 notas bimestrais.
O algoritmo deve calcular a média destas notas, e uma mensagem informando que a média da disciplina nome é média."""

disciplina = input('Qual é o nome da disciplina?')
nota1 = float(input('Qual foi a 1° nota?'))
nota2 = float(input('Qual foi a 2° nota?'))
nota3 = float(input('Qual foi a 3° nota?'))
nota4 = float(input('Qual foi a 4° nota?'))
media = (nota1 + nota2 + nota3 + nota4)/4
print(f'A sua média em {disciplina} foi de {media:.1f}')

