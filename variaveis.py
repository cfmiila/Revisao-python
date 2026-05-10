# Cenário: Uma empresa decidiu dar um bônus de 10% sobre o faturamento total para a
# equipe de vendas. Objetivo: Calcule o valor do bônus e o faturamento final da empresa
# após subtrair esse bônus.
# ● Faturamento inicial: 50.000
# # ● Percentual de bônus: 0.10

# faturamento_inicial=50000
# percentual_bonus= 0.1
# bonus_total= faturamento_inicial * percentual_bonus
# faturamento_liquido= faturamento_inicial - bonus_total
# print("O valor bônus é:",bonus_total)
# print("O Faturamento liquido é:",faturamento_liquido)

# Exercício 2: Controle de Estoque de E-commerce (Logística)
# Cenário: Um e-commerce começou o dia com 250 unidades de um smartphone no
# estoque. Durante o dia, foram vendidos 78 unidades e chegaram mais 100 unidades de um
# # fornecedor. Objetivo: Atualize a variável de estoque e exiba o saldo final.
# estoque= 250
# venda= 78
# reposicao=100
# estoque= estoque-venda+reposicao #redefinir a variavel estoque
# print("Estoque Final:", estoque)

# Exercício 3: Divisão de Cargas (Logística/Transporte)
# Cenário: Uma transportadora precisa levar 1.250 caixas em caminhões pequenos. Cada
# caminhão suporta exatamente 12 caixas. Objetivo: 1. Quantos caminhões sairão
# totalmente cheios? (Use //) 2. Quantas caixas sobrarão para serem enviadas em uma
# última viagem menor? (Use %)

# caixas= 1250
# capacidade_caminhao= 12

# caminhoes_completos= caixas // capacidade_caminhao
# print("Caminhoes completos", caminhoes_completos)
# caminhoes_restantes= caixas % caminhoes_completos
# print("Caminhoes restantes", caminhoes_restantes)

# Exercício 4: Análise de Margem de Lucro (Financeiro)
# Cenário: Uma consultoria faturou R$ 15.000,00 em um projeto. Os custos fixos foram de R$
# 5.000,00 e o imposto sobre o faturamento é de 15%. Objetivo: Calcule o imposto, o lucro
# líquido e a margem de lucro (Lucro / Faturamento). No final, crie uma variável booleana
# chamada meta_atingida que verifica se a margem de lucro é superior a 0.30 (30%).

# faturamento= 15000
# custo_fixo= 5000
# imposto= 0.15

# imposto_fat= faturamento * imposto
# lucro_liquido= faturamento- custo_fixo- imposto_fat
# margem= lucro_liquido / faturamento

# print("Faturamento", faturamento)
# print("Lucro", lucro_liquido)
# print(f"Margem de lucro: {margem *100:.2f}%")



# # meta_atingida= margem > 0.30
# # print("Meta atingida?", meta_atingida)

# if margem > 0.30:
#     meta_atingida= True
#     print("Parabéns! sua meta foi atingida")

# else:
#     meta_atingida=False
#     print("Sinto muito, meta não atingida")

#  Exercício 5: Conversão de Tempo de Contrato (Gestão de Projetos)
# # Cenário: Um contrato de manutenção de software tem a duração de 40 meses. O cliente
# # quer ver esse tempo no formato: "X anos e Y meses". Objetivo: Utilize os operadores de
# # divisão inteira e resto da divisão para converter os 40 meses.

duracao= 40
anos= 40 // 12
meses_sobram= 40 % 12
print("Duração do contrato é de", anos, "anos", meses_sobram, "meses")