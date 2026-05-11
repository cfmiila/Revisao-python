import re


def validar_cnj(numero:str) -> bool: 
    numero= numero.strip()
    padrao= r'^\d{7}-\d{2}\.\d{4}\.\d{1}\.\d{2}\.\d{4}$' #r bruta , ^$
    return bool(re.match(padrao,numero))

# Testes 
assert validar_cnj("0001234-56.2024.8.05.0001") == True  #testes unitarios
assert validar_cnj("0001234-56.2024.8.05.0001 ") == True  
assert validar_cnj("0001234562024.8.05.0001")    == False  
assert validar_cnj("")                            == False
assert validar_cnj("abc")                         == False