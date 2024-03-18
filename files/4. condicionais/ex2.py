'''Solicite 3 numeros e informe qual é o menor'''
n1 = float(input("Digite o n1: "))
n2 = float(input("Digite o n2: "))
n3 = float(input("Digite o n3: "))

if n1 < n2 and n1 < n3:
    print(f"O N1 ({n1:.2f}) é o menor número")
elif n2 < n1 and n2 < n3:
    print(f"O N2 ({n2:.2f}) é o menor número")
elif n3 < n1 and n3 < n2:
    print(f"O N3 ({n3:.2f}) é o menor número")
elif not n1 != n2 and n2 == n3:
    print("Os três números são iguais")