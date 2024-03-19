'''5. Implemente um programa que leia o destino do passageiro, se a viagem inclui retorno
(ida e volta) e informar o preço da passagem conforme a tabela a seguir:'''

print("1 - Região Norte")
print("2 - Região Nordeste")
print("3 - Região Centro-Oeste")
print("4 - Região Sul")

destino = int(input("Digite o número do seu destino: "))


if destino == 1:
    condicao = input("Deseja incluir passagem de volta? Sim (S) ou Não (N)")
    if condicao == "Sim" or condicao == "S" or condicao == "sim" or condicao == "s":
          print("Sua passagem custará R$ 900,00")
    else:
        print("Sua passagem custará R$ 500,00")
elif destino == 2:
    condicao = input("Deseja incluir passagem de volta? Sim (S) ou Não (N)")
    if condicao == "Sim" or condicao == "S" or condicao == "sim" or condicao == "s":
          print("Sua passagem custará R$ 650,00")
    else:
        print("Sua passagem custará R$ 350,00")
elif destino: == 3:
    condicao = input("Deseja incluir passagem de volta? Sim (S) ou Não (N)")
    if condicao == "Sim" or condicao == "S" or condicao == "sim" or condicao == "s":
          print("Sua passagem custará R$ 350,00")
    else:
        print("Sua passagem custará R$ 600,00")
else:
    condicao = input("Deseja incluir passagem de volta? Sim (S) ou Não (N)")
    if condicao == "Sim" or condicao == "S" or condicao == "sim" or condicao == "s":
          print("Sua passagem custará R$ 550,00")
    else:
        print("Sua passagem custará R$ 300,00")