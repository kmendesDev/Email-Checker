import re
import csv

lista_valid_email = []  # Lista para armazenar os e-mails válidos
lista_invalid_email = []  # Lista para armazenar os e-mails inválidos


def verificador_de_e_mail(email):
    # Verifica se o e-mail é válido usando uma expressão regular
    if re.search(r"\b[a-z A-Z 0-9 . _ % + -]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b", email):
        # Adiciona o e-mail à lista de e-mails válidos:
        lista_valid_email.append(email)
    else:
        # Adiciona o e-mail à lista de e-mails inválidos:
        lista_invalid_email.append(email)


arquivo = "D:\Pablinho & Nanda\Documents\Programação\Python\Treinos\Projetos com Python\Verificador de Emails\Dados.csv"  # Especifique o caminho para o arquivo CSV

emails = []  # Inicializando a lista de e-mails

with open(arquivo) as file:
    ler_csv = csv.reader(file)
    for row in ler_csv:
        verificador_de_e_mail(row[2])  # Verifica o e-mail na coluna 2 (índice 2) do CSV
        emails.append(row[2])  # Adiciona o e-mail à lista de e-mails

print("E-mails válidos:")
for email in lista_valid_email:
    print(email)

print("\nE-mails inválidos:")
for email in lista_invalid_email:
    print(email)
