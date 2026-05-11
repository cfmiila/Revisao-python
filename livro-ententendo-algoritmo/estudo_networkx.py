import networkx as nx

# 1 Definindo o dicionário (igual ao do livro)
grafo_manual = {
    "inicio": {"a": 6, "b": 2},
    "a": {"fim": 1},
    "b": {"a": 3, "fim": 5},
    "fim": {}
}

# 2 Criando o objeto do NetworkX (Grafo Direcionado)
G = nx.DiGraph()

# 3 Populando o Grafo
for origem, destinos in grafo_manual.items():
    for destino, peso in destinos.items():
        # Adicionamos uma 'edge' (aresta) com seu peso
        G.add_edge(origem, destino, weight=peso)

# 4 Usando o Dijkstra da biblioteca
caminho = nx.dijkstra_path(G, "inicio", "fim")
custo = nx.dijkstra_path_length(G, "inicio", "fim")

print(f"O caminho mais rápido é: {caminho}")
print(f"O custo total desse caminho é: {custo}")

# 5 Listando os vizinhos de um nodo específico (ex: inicio)
print(f"Os vizinhos do 'inicio' são: {list(G.neighbors('inicio'))}")