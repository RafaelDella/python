'''
3. Criar um jogo de par ou ímpar, onde dois jogadores entram com seu palpite (par ou
ímpar) e seus valores de 1 a 5. Tomar por base os nomes: Jogador 1 e Jogador 2. Caso
um dos valores esteja fora dos parâmetros informados, mostrar uma mensagem
informando que esta rodada não valeu. Caso contrário, informa qual jogador ganhou esta
rodada'''

regra = input("Jogador 1, você prefere Par(Par) ou Impar(Impar)? ")
jogador1 = int(input("Digite um número de 1 - 5: "))
jogador2 = int(input("Digite um número de 1 - 5: "))
numero = (jogador1 + jogador2)%2

if numero != 0:
    print("Deu Impar!!!")
    if regra == "Impar":
        print("Jogador 1 venceuu")
    else:
        print("Jogador 2 venceuu")
else:
    print("Deu Par!!!")
    if regra == "Par":
        print("Jogador 1 venceuu")
    else:
        print("Jogador 2 venceuu")