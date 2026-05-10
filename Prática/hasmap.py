#contar frequência de elementos 


def contar_frequencia(lista):
    contagem = {}
    for item in lista:
        contagem[item] = contagem.get(item, 0) + 1
    return contagem

print(contar_frequencia(["a", "b", "a", "c", "b", "a"]))


# Você percorre a lista uma vez (N vezes).
# Dentro desse loop, você faz operações de busca e inserção no dicionário, que custam O(1)
# .Matematicamente: N \times O(1) = O(N).

def mais_frequente(lista):
    contagem = contar_frequencia(lista)
    return max(contagem, key= contagem.get)

print(mais_frequente([500, 200, 500, 404, 500, 200]))

#ou um disfarçado

from collections import Counter

lista = [500, 200, 500, 404, 500, 200]
print(Counter(lista).most_common(1)[0], [0])

#Escreva uma função que recebe uma string e retorna se ela é um número de processo válido no formato CNJ."
# Formato CNJ: NNNNNNN-DD.AAAA.J.TT.OOOO
# 7 dígitos — dígitos verificadores (2) — ano (4) — ramo da justiça (1) — tribunal (2) — origem (4)

