'''5. Implemente um programa que leia o destino do passageiro, se a viagem inclui retorno
(ida e volta) e informar o preço da passagem conforme a tabela a seguir:'''

print("Seja Bem-vindo a LATAM, estamos com promoção nos vôos nacionais. Faça uma simulação!")

print("1 - Região Norte")
print("2 - Região Nordeste")
print("3 - Região Centro-Oeste")
print("4 - Região Sul")

destino = int(input("Digite o número do seu destino: "))
numeroPassagens = int(input("Digite o número de passagens desejadas: "))
print(f"{destino} e {numeroPassagens}")
if (numeroPassagens > 0) and (0 < destino and destino < 5):
    if destino == 1:
        condicao = input("Deseja incluir passagem de volta? Sim (S) ou Não (N) ").lower()
        if condicao == "s" or condicao == "sim":
            valor = 900 * numeroPassagens
            print(f"Sua passagem custará R$ {valor:.2f}")
        else:
            valor = 500 * numeroPassagens
            print(f"Sua passagem custará R$ {valor:.2f}")
    elif destino == 2:
        condicao = input("Deseja incluir passagem de volta? Sim (S) ou Não (N) ").lower()
        if condicao == "sim" or condicao == "s":
            valor = 650 * numeroPassagens
            print(f"Sua passagem custará R$ {valor:.2f}")
        else:
            valor = 650 * numeroPassagens
            print(f"Sua passagem custará R$ {valor:.2f}")
    elif destino == 3:
        condicao = input("Deseja incluir passagem de volta? Sim (S) ou Não (N) ").lower()
        if condicao == "sim" or condicao == "s":
            valor = 350 * numeroPassagens
            print(f"Sua passagem custará R$ {valor:.2f}")
        else:
            valor = 600 * numeroPassagens
            print(f"Sua passagem custará R$ {valor:.2f}")
    else:
        condicao = input("Deseja incluir passagem de volta? Sim (S) ou Não (N) ").lower()
        if condicao == "sim" or condicao == "s":
            valor = 550 * numeroPassagens
            print(f"Sua passagem custará R$ {valor:.2f}")
        else:
            valor = 300 * numeroPassagens
            print(f"Sua passagem custará R$ {valor:.2f}")
else:
    print("ERROR! INFORMAÇÕES INVÁLIDAS!")