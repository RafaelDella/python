''' Elabore um algoritmo que faça a média bimestral de um aluno e diga se o aluno
foi aprovado (x=> 7), reprovado (x <4) ou recuperação ( 4 <= x > 7) '''

nome = input("Digite o nome do aluno: ")
disciplina = input("Digite a disciplina: ")
n1 = float(input("Digite a n1: "))
n2 = float(input("Digite a n2: "))
n3 = float(input("Digite a n3: "))
n4 = float(input("Digite a n4: "))

media = (n1 + n2 + n3 + n4)/4
if media < 0:
    media = 0

if media > 7:
    print(f"{nome} foi aprovado, em {disciplina}, com {media:.1f}")
elif media < 4:
    print(f"{nome} foi reprovado, em {disciplina}, com {media:.1f}")
else:
    print(f"{nome} foi para recuperação, em {disciplina}, com {media:.1f}")