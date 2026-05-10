#agrupar por propriedade (dicionário de listas)


processos = [
    {"numero": "001", "status": "ativo"},
    {"numero": "002", "status": "arquivado"},
    {"numero": "003", "status": "ativo"},
    {"numero": "004", "status": "suspenso"},
    {"numero": "005", "status": "arquivado"},
]

def agrupar_por(lista, chave):
    grupos= {}
    for item in lista:
        valor = item[chave]
        if valor not in grupos:
            grupos[valor]= []
        grupos[valor].append(item)
    return grupos


agrupar_por(processos, "status")
