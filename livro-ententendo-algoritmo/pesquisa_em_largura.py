#Implementando o grafo:
#um grafo é uma estrutura de dados que representa um conjunto de objetos (vértices)
# e as conexões entre eles (arestas). 
# No exemplo abaixo, estamos criando um grafo usando um dicionário em Python, 
# onde cada chave é um vértice e o valor associado é uma lista de vértices adjacentes (conexões).
# a ordem que adicionamos os vértices e as conexões não importa,
# o importante é que o grafo represente corretamente as relações entre os vértices.
# as tabelas hash não são ordenadas 

#implementando o algoritmo 

grafo = {}
grafo ["voce"] = ["alice", "bob", "claire"]
grafo ["alice"] = ["anuj", "peggy"]
grafo ["bob"] = ["anuj", "peggy"]
grafo ["claire"] = ["thom", "jonny"]
grafo ["anuj"] = []
grafo ["peggy"] = []
grafo ["thom"] = []
grafo ["jonny"] = []

def pessoa_e_vendedor(nome):    
    return nome[-1] == "m" #essa função é um exemplo simples que verifica se o nome da pessoa termina com a letra "m", indicando que ela é uma vendedora.

from collections import deque
fila_de_pesquisa = deque() #1 criamos uma nova lista
fila_de_pesquisa += grafo ["voce"] #2 dicionamos os vizinhos do vértice "você" à fila de pesquisa.



def pesquisa(nome):
    fila_de_pesquisa = deque()
    fila_de_pesquisa += grafo [nome]
    verificadas = []  # esse vetor é a forma pela qual você mantem o registro das pessoas que já foram verificadas, para evitar loops infinitos.

    while fila_de_pesquisa: #enquanto a fila de pesquisa não estiver vazia
        pessoa = fila_de_pesquisa.popleft() #remova a primeira pessoa da fila de pesquisa
        if pessoa not in verificadas: #se a pessoa ainda não foi verificada
            if pessoa_e_vendedor(pessoa): #verifique se a pessoa é vendedora
                print(f"{pessoa} é uma vendedora!")
                return True
            else:
                fila_de_pesquisa += grafo [pessoa] #se a pessoa não for vendedora, adicione seus vizinhos à fila de pesquisa
                verificadas.append(pessoa) #marque a pessoa como verificada

    return False #se a fila de pesquisa estiver vazia e nenhuma vendedora tiver sido encontrada, retorne falso

pesquisa ("voce")

# a complexidade desse algoritmo é calculada somando dois fatores: (Vértices/Pessoas):
# Você mantém a lista verificadas para garantir que cada pessoa seja analisada apenas uma vez. 
# Adicionar uma pessoa na lista leva tempo constante O(1).
# Para cada pessoa que você tira da fila, 
# você percorre todas as conexões (setas) dela para adicionar os vizinhos.
# Assim, a pesquisa em largura tem uma complexidade de O(V + A), onde V é o número de vértices (pessoas) e A é o número de arestas (conexões).
# Se você não tivesse usar a lista verificadas,
# o código poderia ficar preso em um loop infinito (se a Ana fosse amiga do Beto e o Beto fosse amigo da Ana), 
# e o tempo de execução seria impossível de calcular!


# Capítulo 6 - Pesquisa em Largura
# Recapitulação:

# • A pesquisa em largura lhe diz se há um caminho de A para B.
# • Se esse caminho existir, a pesquisa em largura lhe dará o caminho mínimo.
# • Se você tem um problema do tipo “encontre o menor X”, tente modelar o seu problema 
#   utilizando grafos e use a pesquisa em largura para resolvê-lo.
# • Um dígrafo contém setas e as relações seguem a direção das setas 
#   (Rama -> Adit significa “Rama deve dinheiro a Adit”).
# • Grafos não direcionados não contêm setas, e a relação acontece nos dois sentidos 
#   (Ross – Rachel significa “Ross namorou Rachel e Rachel namorou Ross”).
# • Filas são FIFO (primeiro a entrar, primeiro a sair).
# • Pilhas são LIFO (último a entrar, primeiro a sair).
# • Você precisa verificar as pessoas na ordem em que elas foram adicionadas à lista 
#   de pesquisa. Portanto a lista de pesquisa deve ser uma fila; caso contrário, 
#   você não obterá o caminho mínimo.
# • Cada vez que você precisar verificar alguém, procure não verificá-lo novamente. 
#   Caso contrário, poderá acabar em um