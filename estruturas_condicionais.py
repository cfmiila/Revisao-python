# Exercício 1: Validação de Investimento (Setor Financeiro) Uma corretora de valores
# quer automatizar a recomendação básica de perfil. Crie um programa que peça ao usuário o
# valor que ele deseja investir.
# 1. Se o valor for menor que R$ 1.000,00, exiba: "Perfil iniciante: Sugerimos Tesouro
# Direto".
# 2. Se o valor for entre R$ 1.000,00 e R$ 5.000,00 (inclusive), exiba: "Perfil moderado:
# Sugerimos Fundos Imobiliários".
# 3. Se o valor for acima de R$ 5.000,00, exiba: "Perfil arrojado: Sugerimos Ações".
# *Lembre-se de tratar o input caso o usuário digite "R$" ou use vírgula.*

print("##### Exercicio 1 #### ")

valor= input("Digite o valor que vc quer investir: ")
valor = valor.replace("R$", "").replace(".", "").replace(",", ".")
valor = float(valor)

if valor < 1000:
    print("Perfil iniciante: Sugerimos Tesouro Direto")
elif valor <=5000:
    print("Perfil moderado: Sugerimos Fundos Imobiliários")
else:
    print("Perfil arrojado: Sugerimos Ações")
