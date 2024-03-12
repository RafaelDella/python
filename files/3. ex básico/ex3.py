"""Crie um algoritmo que calcule o valor da refeição e 
pergunte ao cliente se ele deseja pagar a taxa de serviço (10%)"""

prato = input('Digite o prato que foi consumido: ')
quantidade = float(input(f'Digite a quantidade de {prato} consumido: '))
preco = float(input(f'Digite o valor de {prato}: '))
total = quantidade * preco

taxa_garcom = input('Você permite incluir a taxa de serviço (10%) ao valor de consumo? Aceito(Sim) ou à Não Aceito(Não)')
if taxa_garcom == 'Sim':
    total = total + (total * 0.15)

print(f'O total a ser pago é R${total:.2f}')
