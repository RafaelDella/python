rendimento_mensal = float(input("Digite o seu rendimento mensal: "))
dependentes = int(input("Digite o número de dependentes: "))
valor_pensao_alimenticia = float(input("Digite o valor da pensão alimenticia: "))
outras_deducoes = float(input("Digite o valor de outas deduções: "))

base_deducao = rendimento_mensal - (189.59 * dependentes) + valor_pensao_alimenticia + outras_deducoes

faixa1 = 1903.98
faixa2 = 2826.65
faixa3 = 3751.05
faixa4 = 4664.68
faixa5 = faixa4
'''
if base_deducao <= faixa1:
    aliquota = 0
    print(f"O seu Imposto de Renda é: {base_deducao:.2f} com uma Aliquota de {aliquota}%")
elif base_deducao > faixa1 and base_deducao < faixa2:
    aliquota = 0.075
    base_deducao =  base_deducao + (base_deducao * aliquota)
    print(f"O seu Imposto de Renda é: {base_deducao:.2f} com uma Aliquota de {aliquota * 100}%")
elif base_deducao > faixa2 and base_deducao < faixa3:
    aliquota = 0.15
    base_deducao = base_deducao + (base_deducao * aliquota) + 169.44
    print(f"O seu Imposto de Renda é: {base_deducao:.2f} com uma Aliquota de {aliquota * 100}%")
elif base_deducao > faixa3 and base_deducao < faixa4:
    aliquota = 0.225
    base_deducao = base_deducao + (base_deducao * aliquota) + 169.44 + 381.44
    print(f"O seu Imposto de Renda é: {base_deducao:.2f} com uma Aliquota de {aliquota * 100}%")
elif base_deducao > faixa5:
    aliquota = 0.275
    base_deducao = base_deducao + (base_deducao * aliquota) + 169.44 + 381.44 + 662.77
    print(f"O seu Imposto de Renda é: {base_deducao:.2f} com uma Aliquota de {aliquota * 100}%")
'''
valor_final = 0
if base_deducao > faixa1:
    if(base_deducao <  faixa2):
        aliquota = 0.075
        valor_final = (base_deducao - faixa1) * aliquota
    else:
        aliquota = 0.075
        valor_final = (faixa2 - faixa1) * aliquota

