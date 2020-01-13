"""
Lendo Arquivos CSV

CSV - Comma Separeted Values - Valores Separados por Vírgula

# Separador por vírgula
1, 2, 3, 4, 5, 6
"geek", "University", "Python"

# Separador por ponto e vírgula
1; 2; 3; 4; 5; 6
"geek"; "University"; "Python"

# Separador por espaço
1 2 3 4 5 6
"geek" "University" "Python"

http://dados.gov.br/dataset

# Possível de se trabalhar, mas não é o ideal (trabalhoso)

with open('lutadores.csv', encoding="utf8") as arquivo:
    dados = arquivo.read()
    # print(type(dados))
    dados = dados.split(',')[2:]
    print(dados)

O python tem 2 formas diferentes para ler dados em arq CSV:
    - render -> permite que iteremos sobre as linhas do arquivo CSV como lista;
    - DictReader -> Permite que iteremos sobre as linhas do arquivo CSV como OrderedDicts;

# Reader

from csv import reader

with open('lutadores.csv', encoding="utf-8") as arquivo:
    leitor_csv = reader(arquivo)
    next(leitor_csv)  # Pular o cabeçalho
    for linha in leitor_csv:
        #  Cada linha é uma lista
        print(f'{linha [0]} nasceu no(a)(s) {linha[1]} e mede {linha[2]} centimetros')


# DictReader

from csv import DictReader

with open('lutadores.csv', encoding="utf-8") as arquivo:
    leitor_csv = DictReader(arquivo)
    for linha in leitor_csv:
        # Cada linha é um OrderedDict
        print(f"{linha['Nome']} nasceu no(a)(s) {linha['País']} e mede {linha['Altura (em cm)']}")

"""


# DictReader com outro separador

from csv import DictReader

with open('lutadores.csv', encoding="utf-8") as arquivo:
    leitor_csv = DictReader(arquivo, delimiter=',')
    for linha in leitor_csv:
        # Cada linha é um OrderedDict
        print(f"{linha['Nome']} nasceu no(a)(s) {linha['País']} e mede {linha['Altura (em cm)']}")
