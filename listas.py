# Exercício 1: Dashboard de Vendas (Análise de Dados) Você recebeu uma lista com as
# vendas diárias de uma equipe: vendas = [1500, 2000, 800, 3500, 1200]. Crie um
# programa que exiba um pequeno relatório contendo:
# 1. O total de vendas na semana.
# 2. A média de vendas diária.
# 3. O valor da melhor venda e da pior venda do período.

print("##### Exercicio 1 #### ")

vendas = [1500, 2000, 800, 3500, 1200]

total_vendas= sum(vendas)
qtd_dias = len(vendas)
media_vendas= total_vendas / qtd_dias
maior_venda= max(vendas)
menor_venda= min(vendas)
print(f"Total: {total_vendas}, Média de Vendas: {media_vendas},\
       Maior Venda: {maior_venda}, Menor Venda: {menor_venda}")

print("##### Exercicio 2 #### ")

# Exercício 2: Gestão de Estoque (Edição e Verificação) Uma loja de eletrônicos possui os
# seguintes produtos: estoque = ["monitor", "teclado", "mouse", "headset"].
# O gerente pediu para:
# 1. Adicionar o item "webcam" ao final da lista.
# 2. O "teclado" teve seu nome atualizado para "teclado mecanico". Faça essa
# alteração na lista.
# 3. Verificar se "impressora" está no estoque. O programa deve exibir True ou
# False.
# 4. Remover o "mouse" da lista, pois saiu de linha.
estoque = ["monitor", "teclado", "mouse", "headset"]
estoque.append("webcam")
print(estoque)
posicao_teclado = estoque.index("teclado")
estoque[posicao_teclado] = "teclado mecânico"
print(estoque)

impressora_no_estoque = "impressora" in estoque
print("Impressora no estoque?", impressora_no_estoque)

estoque.remove("mouse")
print(estoque)



# se fosse com pop- posicao_mouse = estoque.index("mouse")
# estoque.pop(posicao_mouse)
# print(estoque)





print("##### Exercicio 3 #### ")
# Exercício 3: Organização de Preços (Ordenação e Slicing) Uma importadora listou os
# preços de frete em dólar: fretes = [50, 80, 20, 150, 40]. Para apresentar em uma
# reunião, você deve:
# 1. Ordenar a lista do maior para o menor preço.
# 2. Pegar os 2 fretes mais caros  e armazenar em uma nova
# lista chamada top_fretes.
# 3. Exibir a lista original ordenada e a lista dos top_fretes.

fretes = [50, 80, 20, 150, 40]
fretes.sort(reverse=True)
print(fretes)
top_fretes = fretes[:2]
print(top_fretes)



print("##### Exercicio 4 #### ")

# Exercício 4: Sistema de Logística (Busca e Extensão) A empresa "LogTrack" tem uma
# rota de entregas: rota = ["Sao Paulo", "Campinas", "Jundiai",
# "Sorocaba"]. Novas cidades foram adicionadas por uma empresa parceira:
# novas_cidades = ["Itu", "Valinhos"]. Seu script deve:
# 1. Unir as duas listas em uma só 
# 2. Identificar em qual posição (índice) está a cidade de "Sorocaba".
# 3. Exibir a lista completa e a posição encontrada.
# 4. Exibir uma mensagem final: “Sorocaba é a Xa cidade da rota”

rota = ["Sao Paulo", "Campinas", "Jundiai", "Sorocaba"]
novas_cidades = ["Itu", "Valinhos"]

rota.extend(novas_cidades)
print(rota)
posicao_sorocaba = rota.index("Sorocaba") + 1
print(f"Sorocoba é a {posicao_sorocaba} a cidade da rota")








print("##### Exercicio 5 #### ")

# Exercício 5: Atualização de Preços Interativa (Input + Lista) Você tem uma lista de
# preços de produtos: precos = [100.0, 250.0, 500.0] e uma com o nome: vinhos
# = ["Branco", "Tinto","Champagne"]. Crie um programa interativo que:
# 1. Peça para o usuário digitar qual o nome do produto.
# 2. Peça para o usuário digitar o novo preço.
# 3. Atualize o preço na lista e exiba as listas completas com os nomes e os preços


precos = [100.0, 250.0, 500.0]
vinhos = ["Branco", "Tinto","Champagne"]

vinho_escolhido= input("Digite o nome do produto: ") 
novo_preco= input("Digite um novo preço: ")
novo_preco = novo_preco.replace("R$", "").replace(".", "").replace(",", ".")
novo_preco= float(novo_preco)


posicao_vinho= vinhos.index(vinho_escolhido)
precos[posicao_vinho]= novo_preco

print(vinhos)
print(precos)

