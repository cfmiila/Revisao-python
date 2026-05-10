# Exercício 1: Relatório de Margem de Lucro (Setor Financeiro) Uma empresa de varejo
# precisa de um resumo rápido sobre a performance de um produto. Dado o faturamento de
# R$ 45.000,00 e o custo de R$ 23.500,00, crie um programa que calcule o lucro e a margem
# de lucro (lucro dividido pelo faturamento). Exiba uma mensagem formatada onde o lucro
# use o separador de milhar e duas casas decimais, e a margem seja exibida como uma
# porcentagem inteira.
print("##### Exercicio 1 #### ")

fat= 45000
custo= 23500
lucro= fat - custo
margem= lucro / fat

print(f"Lucro: {lucro:,.2f}, Margem: {margem:.0%}")

# Exercício 2: Padronização de Dados de CRM (Setor de Vendas) Um vendedor cadastrou
# um cliente com os dados desorganizados no sistema: nome = " mArCoS aNtOnIo
# rOcHa " e email = " MARCOS.ROCHA@GMAIL.COM ". Para evitar duplicidade e erros
# de envio, você deve:
# 1. Remover os espaços extras no início e fim das duas variáveis.
# 2. Deixar o nome apenas com as primeiras letras de cada palavra em maiúsculo
# (formato de nome próprio).
# 3. Deixar o e-mail todo em letras minúsculas. Exiba os resultados finais no console.
print("##### Exercicio 2 #### ")

nome =  " mArCoS aNtOnIo rOcHa " 
email = " MARCOS.ROCHA@GMAIL.COM"

nome = nome.strip() .title()
print(nome)

email = email.strip()
email = email.lower()
print(email)

# Exercício 3: Migração de Servidor de E-mail (Setor de TI) Sua empresa mudou de nome
# e todos os funcionários que usavam o domínio @empresa.com.br agora devem usar o
# domínio @grupocorp.com. O e-mail do funcionário é andre_silva@empresa.com.br.
# Crie um código que substitua automaticamente o domínio antigo pelo novo e exiba o novo
 # endereço de e-mail.

# email= "andre_silva@empresa.com.br"
# novo_dominio= "@grupocorp.com"
# posicao_arroba = email.find("@")
# print(posicao_arroba)

# email = email[:11] + novo_dominio
# print(email)
#e uma forma mais simples seria com- email = email.replace("@empresa.com.br","@grupocorp.com")
#em uma situação maior ficaria assim:

# funcionarios = [
#     "andre_silva@empresa.com.br",
#     "maria_santos@empresa.com.br",
#     "val_silva@empresa.com.br"

# ]

# def migrar_dominio(lista_emails):
#     novos_emails = []
#     for email in lista_emails:
#         posicao_arroba = email.find("@")
#         novo_email = email[:posicao_arroba] + "@grupocorp.com"
#         novos_emails.append(novo_email)
#     return novos_emails

# lista_atualizada = migrar_dominio(funcionarios)

# for email in lista_atualizada:
#     print(email)

# Exercício 4: Extração de Username para Log (Setor de Segurança) Para criar um log de
# acessos, o sistema precisa extrair apenas a parte do nome do usuário de um e-mail
# corporativo (tudo o que vem antes do @). Dado o e-mail
# beatriz.oliveira@grupocorp.com, use a função .find() e o fatiamento de texto
# para extrair e exibir apenas o nome beatriz.oliveira.
print("##### Exercicio 4 #### ")

email= "beatriz.oliveira@grupocorp.com"
posicao_a = email.find("@")
username= email[:posicao_a]
print(username)

# Exercício 5: Person   lização de E-mail de Marketing (Setor de Marketing) O marketing
# quer enviar um e-mail de boas-vindas. O cliente forneceu o nome completo: lucas
# ferreira souza. Você deve extrair apenas o primeiro nome para usar na saudação (ex:
# "Olá, Lucas!"). O código deve:
# 1. Encontrar a posição do primeiro espaço.
# 2. Fatiar o texto para pegar apenas o primeiro nome.
# 3. Formatar o nome com a primeira letra maiúscula.
# 4. Exibir a mensagem: "Olá, [Primeiro Nome], seja bem-vindo ao nosso clube!"
print("##### Exercicio 5 #### ")

mensagem = "Olá, [Primeiro Nome], seja bem vindo ao nosso clube! "
nome= "lucas ferreira souza"
posicao_espaco = nome.find(" ")
pri_nome= nome[:posicao_espaco].capitalize()

mensagem = mensagem.replace("[Primeiro Nome]", pri_nome)
print(mensagem)