'''
3. Criar um jogo de par ou ímpar, onde dois jogadores entram com seu palpite (par ou
ímpar) e seus valores de 1 a 5. Tomar por base os nomes: Jogador 1 e Jogador 2. Caso
um dos valores esteja fora dos parâmetros informados, mostrar uma mensagem
informando que esta rodada não valeu. Caso contrário, informa qual jogador ganhou esta
rodada'''

regra = input("Jogador 1, você prefere Par(Par) ou Impar(Impar)? ").lower()
jogador1 = int(input("Digite um número de 1 - 5: "))
jogador2 = int(input("Digite um número de 1 - 5: "))

if (0 < jogador1 and jogador1 < 6) and (0 < jogador2 and jogador2 < 6):
    numero = (jogador1 + jogador2)%2
    if numero != 0:
        print("Deu Impar!!!")
        if regra == "impar":
            print("Jogador 1 venceu!!")
        else:
            print("Jogador 2 venceu!!")
    else:
        print("Deu Par!!!")
        if regra == "par":
            print("Jogador 1 venceu!!")
        else:
            print("Jogador 2 venceu!!")
else:
    print("Escolha de número inválido! Renicie o jogo.")