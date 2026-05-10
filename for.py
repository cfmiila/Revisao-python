# Exercício 1: Automação de Convites (Setor de Eventos/RH) A empresa terá um
# treinamento e você precisa simular o envio de 10 lembretes no console fazendo a contagem
# regressiva para aparecer no sistema da empresa. Use a função range() para imprimir 10
# vezes a mensagem: "Lembrete: O treinamento de Python começa em X minutos.

for i in range(10):
    tempo_falta = 10 - i
    print(f"Faltam {tempo_falta} minutos para começar o treinamento")


#exercicio 2
# Exercício 2: Cálculo de Comissão Progressiva (Setor de Vendas) Você tem uma lista de
# vendas de um vendedor: vendas = [2000, 5000, 1000, 8000, 3000]. A regra de
# comissão é:
# ● Vendas acima de R$ 4.000,00: comissão de 10%.
# ● Vendas até R$ 4.000,00: comissão de 5%. Crie um programa que percorra a lista e,
# ao final, exiba o valor total que o vendedor receberá de comissão.


vendas = [2000, 5000, 1000, 8000, 3000]

comissao_total = 0
for venda in vendas:
    if venda > 400:
        comissao= 0.1
else:
    comissao = 0.5
    comissao_total += comissao * venda

print(f"Comissão total de {comissao_total:.2f}")