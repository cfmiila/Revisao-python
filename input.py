# Exercício 1: Calculadora de Imposto sobre Vendas (Setor Fiscal) Uma empresa de
# serviços precisa calcular o imposto de 15% sobre o valor bruto de uma nota fiscal. Como o
# valor muitas vezes vem copiado de planilhas com "R$" e vírgula, seu programa deve:
# 1. Pedir para o usuário digitar o valor bruto (Ex: R$ 5.000,00).
# 2. Limpar o texto removendo o "R$" e trocando a vírgula por ponto.
# 3. Converter para número decimal (float).
# 4. Calcular o valor do imposto (15% do valor bruto).
# 5. Exibir uma mensagem formatada com f-string mostrando o valor do imposto com
 # duas casas decimais.

# print("##### Exercicio 1 #### ")

# fat= input("Digite o faturamento: ")
# fat = fat.replace("R$", "").replace(".", "").replace(",", ".")
# fat_numerico = float(fat)
# percn_imposto = 0.15
# imposto = fat_numerico * percn_imposto
# print(f"O valor do imposto é:{imposto: .2f}")

# print("##### Exercicio 2 #### ")
# mensagem= "Cadastro concluído: [Primeiro Nome]. Email de acesso: [Email padronizado]"
# Exercício 2: Sistema de Cadastro de Colaborador (Setor de RH) Ao cadastrar um novo
# funcionário, o RH precisa extrair o primeiro nome para criar um crachá e padronizar o
# e-mail. Crie um programa que:
# 1. Peça o nome completo do colaborador.
# 2. Peça o e-mail pessoal do colaborador.
# 3. Extraia o primeiro nome (deixe-o com a primeira letra maiúscula).
# 4. Padronize o e-mail (remova espaços extras e deixe tudo em letras minúsculas).
# 5. Exiba a mensagem: "Cadastro concluído: [Primeiro Nome]. E-mail de acesso: [E-mail
# padronizado]".

messages = "Olá [Primeiro Nome], seu cadastro foi realizado com o e-mail: Email padronizado."

nome = input("Digite seu nome completo: ")
email = input("Digite seu email pessoal: ")

nome = nome.strip()
email = email.strip()

posicao_espaco = nome.find(" ")

pri_nome = nome[:posicao_espaco].capitalize()
mensagem = messages.replace("[Primeiro Nome]", pri_nome).replace("Email padronizado", email)

print(mensagem)