"""Estender o exercício 4 anterior informando que para pagamento à vista tem
15% de desconto, calculando e exibindo este valor."""

produto = input('Qual é o produto desejado?')
quantidade = float(input(f'Qual a quantidade de {produto} você deseja?'))
preco = float(input(f'Quanto que custa uma unidade de {produto}'))
total = quantidade * preco

avista = input('Super oferta!! A vista possui 15% de desconto!!! Pagar à vista(Sim) ou à prazo(Não)')
if avista == 'Sim':
    total = total - (total * 0.15)

print(f'O total a ser pago é R${total:.2f}')
