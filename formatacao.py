'''Elabore um algoritmo que solicite dois números ao usuário e exibe a soma deste números

num1 = float(input("Escolha um número"))
num2 = float(input("Escolha outr número"))
soma = num1 + num2
print(f'A soma de {num1} e {num2} é {soma}')'''

"""Elaborar um algoritmo que solicita ao usuário seu ano de nascimento e calcula sua idade com relação ao ano de 2020,
sendo que o usuário já fez aniversário neste ano

nascimento = int(input("Em qual ano você nasceu?"))
print(f'Em 2020, você tinha {2020-nascimento}')
"""

'''
Elaborar um algoritmo que solicita ao usuário o nome de uma disciplina e suas 4 notas bimestrais. 
O algoritmo deve calcular a média destas notas, e uma mensagem informando que a média da disciplina nome é média.

disciplina = input('Qual é o nome da disciplina?')
nota1 = float(input('Qual foi a 1° nota?'))
nota2 = float(input('Qual foi a 2° nota?'))
nota3 = float(input('Qual foi a 3° nota?'))
nota4 = float(input('Qual foi a 4° nota?'))
media = (nota1 + nota2 + nota3 + nota4)/4
print('A média de ' +disciplina+ f' foi de {media}')
'''

"""Elaborar um algoritmo que solicita o nome de um produto, seu valor e
quantidade, informando o valor de compra calculado.

produto = input('Qual é o produto desejado?')
quantidade = int(input(f'Qual a quantidade de {produto} você deseja?'))
preco = float(input(f'Quanto que custa uma unidade de {produto}'))
total = quantidade * preco
print(f'O total a ser pago, de {produto}, é R${total}')"""

"""Estender o exercício 4 anterior informando que para pagamento à vista tem
15% de desconto, calculando e exibindo este valor.

produto = input('Qual é o produto desejado?')
quantidade = int(input(f'Qual a quantidade de {produto} você deseja?'))
preco = float(input(f'Quanto que custa uma unidade de {produto}'))
total = quantidade * preco

avista = input('Super oferta!! A vista possui 15% de desconto!!! Pagar à vista(Sim) ou à prazo(Não)')
if avista != 'Não':
    total = total - (total * 0.15)

print(f'O total a ser pago, de {produto}, é R${total}')"""
