"""
4. Implemente um programa que calcule o que deve ser pago por um produto,
considerando o preço normal de etiqueta e a escolha da condição de pagamento. Utilize
os códigos da tabela a seguir para ler qual a condição de pagamento escolhida e efetuar o
cálculo adequado."""
"""
Código Condição de pagamento
• 1 – À vista em dinheiro ou cheque, recebe 10% de desconto
• 2 – À vista no cartão de crédito, recebe 15% de desconto
• 3 – Em duas vezes, preço normal de etiqueta sem juros
• 4 – Em duas vezes, preço normal de etiqueta mais juros de 10%
"""

"""Crie um algoritmo que calcule o valor da refeição e 
pergunte ao cliente se ele deseja pagar a taxa de serviço (10%)"""

prato = input('Digite o prato que foi consumido: ')
quantidade = float(input(f'Digite a quantidade de {prato} consumido: '))
preco = float(input(f'Digite o valor de {prato}: '))
total = quantidade * preco

print("Forma de pagamento: ")
print("1 - À vista em dinheiro ou cheque, recebe 10% de desconto ")
print("2 - À vista no cartão de crédito, recebe 15% de desconto ")
print("3 - Em duas vezes, preço normal de etiqueta sem juros ")
print("4 - Em duas vezes, preço normal de etiqueta mais juros de 10% ")

pagamento = int(input("Selecione (1-4) uma forma de pagamento!"))
if pagamento == 1:
    total = total - (total * 0.10)
    print(f"O valor da sua compra é de {total:.2f}")
elif pagamento == 2:
    total = total - (total * 0.15)
    print(f"O valor da sua compra é de {total:.2f}")
elif pagamento == 3:
    print(f"O valor da sua compra é de {total:.2f}")
else:
    total = total + (total * 0.10)
    print(f"O valor da sua compra é de {total:.2f}")
