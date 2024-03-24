""" 4. Implemente um programa que calcule o que deve ser pago por um produto,
considerando o preço normal de etiqueta e a escolha da condição de pagamento. Utilize
os códigos da tabela a seguir para ler qual a condição de pagamento escolhida e efetuar o
cálculo adequado."""

produto = input('Digite o produto desejado: ')
quantidade = float(input(f'Digite a quantidade de {produto} desejado: '))
preco = float(input(f'Digite o valor da peça: '))
total = quantidade * preco

print("Forma de pagamento: ")
print("1 - À vista em dinheiro ou cheque, recebe 10% de desconto ")
print("2 - À vista no cartão de crédito, recebe 15% de desconto ")
print("3 - Em duas vezes, preço normal de etiqueta sem juros ")
print("4 - Em duas vezes, preço normal de etiqueta mais juros de 10% ")

pagamento = int(input("Selecione (1-4) uma forma de pagamento: "))
if pagamento == 1:
    total = total - (total * 0.10)
    print("Opção de pagamento selecionada: Dinheiro")
    print(f"O valor total da sua compra é de {total:.2f}")
elif pagamento == 2:
    total = total - (total * 0.15)
    print("Opção de pagamento selecionada: Crédito")
    print(f"O valor total da sua compra é de {total:.2f}")
elif pagamento == 3:
    print("Opção de pagamento selecionada: 2x sem juros")
    print(f"O valor total da sua compra é de {total:.2f}")
elif pagamento == 4:
    total = total + (total * 0.10)
    print("Opção de pagamento selecionada: 2x com um acressio de 10%")
    print(f"O valor total da sua compra é de {total:.2f}")
else:
    print("Opção inválida!")