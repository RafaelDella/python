"""Elaborar um algoritmo que solicita o nome de um produto, seu valor e
quantidade, informando o valor de compra calculado."""

produto = input('Qual é o produto desejado?')
quantidade = float(input(f'Digite a quantidade de {produto}: '))
preco = float(input(f'Digite o valor do produto: '))
total = quantidade * preco
print(f'O total a ser pago, em {produto}, é R${total:.2f}')
