"""
Escrevendo em Arquivos CSV

reader() (Leitor), writer() (escritor)

writerow() -> Escreve uma linha

# writer() -> gera um objeto par que possamos escrever em um arquivo csv. Utilizamos o método
# writerow() -> para escrever cada linha. Este método recebe uma lista.


from csv import writer

with open('filmes.csv', 'w', encoding='utf-8') as arquivo:
    escritor_csv = writer(arquivo)
    filme = None
    escritor_csv.writerow(['Titulo', 'Gênero', 'Duração'])
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o Gênero: ')
            duracao = input('Informe a duração (em minutos): ')
            escritor_csv.writerow([filme, genero, duracao])
"""

# DictWriter
# OBS: As chaves do dicionario devem ser a mesmas utilizadas como cabeçalho

from csv import DictWriter

with open('filmes3.csv', 'w', encoding='utf-8') as arquivo:
    cabecalho = ['Titulo', 'Gênero', 'Duração']
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
    escritor_csv.writeheader()
    filme = None
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o Gênero: ')
            duracao = input('Informe a duração (em minutos): ')
            escritor_csv.writerow({'Titulo': filme, 'Gênero': genero, 'Duração': duracao})
