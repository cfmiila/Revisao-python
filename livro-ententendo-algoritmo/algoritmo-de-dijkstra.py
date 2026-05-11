# O algoritmo de dijkstra é usado para calcular o valor minimo para um grafo ponderado
# ele funciona quando todos os pesos são positivos (tempo)
# se o grafo tiver pesos negativos, use o algoritom de Bellman-ford

# grafo
grafo = {}
grafo["inicio"] = {}
grafo["inicio"]["a"] = 6
grafo["inicio"]["b"] = 2

grafo["a"] = {}
grafo["a"]["fim"] = 1

grafo["b"] = {}
grafo["b"]["a"] = 3
grafo["b"]["fim"] = 5

grafo["fim"] = {} # o vertice final n tem vizinhos 

# tabelas
infinito = float("inf") # representa o infinito, ou seja, um valor muito grande que não pode ser alcançado
custos = {}
custos["a"] = 6
custos["b"] = 2
custos["fim"] = infinito 

pais = {}
pais["a"] = "inicio"
pais["b"] = "inicio"
pais["fim"] = None

processados = [] # essa lista é usada para manter o registro dos vértices que já foram processados, para evitar loops infinitos.

#função para encontrar o vértice com o custo mais baixo que ainda não foi processado
def ache_no_custo_mais_baixo(custos):
    custo_mais_baixo = float("inf")
    nodo_mais_barato = None
    for nodo in custos: # para cada nodo nos custos
        custo = custos[nodo] # obtemos o custo do nodo
        if custo < custo_mais_baixo and nodo not in processados: # se o custo do nodo for menor do que o custo mais baixo encontrado até agora e o nodo ainda não foi processado
            custo_mais_baixo = custo # atualizamos o custo mais baixo
            nodo_mais_barato = nodo # atualizamos o nodo mais barato
    return nodo_mais_barato # retornamos o nodo mais barato encontrado

# o algoritmo de dijkstra 
nodo = ache_no_custo_mais_baixo(custos) # encontramos o vértice com o custo mais baixo que ainda não foi processado

while nodo is not None:
    custo = custos[nodo] # obtemos o custo do vertice atual
    vizinhos = grafo[nodo] # obtemos os vizinhos do vertice atual
    for vizinho in vizinhos.keys(): # para cada vizinho do vertice atual
        novo_custo = custo + vizinhos[vizinho] # calculamos o custo para chegar ao vizinho através do vertice atual
        if custos[vizinho] > novo_custo: # se o custo calculado for menor do que o custo atual registrado para o vizinho
            custos[vizinho] = novo_custo # atualizamos o custo para o vizinho
            pais[vizinho] = nodo # atualizamos o pai do vizinho para o vertice atual

    processados.append(nodo) # marcamos o vertice atual como processado
    nodo = ache_no_custo_mais_baixo(custos) # encontramos o próximo vertice com o custo mais baixo que ainda não foi processado

print(f"Custo final: {custos['fim']}")

# a complexidade do algoritmo de dijkstra é O(E log V), onde E é o número de arestas e V é o número de vértices.