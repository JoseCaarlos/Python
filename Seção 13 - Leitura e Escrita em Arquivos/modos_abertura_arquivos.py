"""
Modos de Abertura de Arquivo

r -> Abre para Leitura - padrão
w -> Abre para escrita - Sobreescreve caso o arquivo já exista
x -> Abre para escrita somente se o arquivo não existir. Caso o arquivo exista. gera FileExistError
a -> Abre para escrita, adicionando o contéudo ao final do arquivo.
+ -> Abre para o modo de atualização leitura e escrita. Temos o controle do cursor

OBS: Abrindo no modo 'a' -> Append, se o arquivo não existir será criado. Caso exista
o novo contéudo será adicionado ao final do arquivo sempre. Com o modo 'a' não controlamos o cursor.


http://docs.python.org/3/library/functions.html#open

Exemplo X

try:
    with open('university.txt', 'x') as arq:
        arq.write('teste de comando.\n')
except FileExistsError:
    print('Arquivo já existe')

# Exemplo A

with open('frutas.txt', 'a') as arq:
    while True:
        fruta = input('Digite uma fruta ou sair: ')
        if fruta != 'sair':
            arq.write(fruta + '\n')
        else:
            break

# Exemplo r+
with open('outro.txt', 'r+') as arq:
    #  arq.seek(0)
    arq.write('adicionada\n')
    arq.seek(11)
    arq.write('2 linha\n')
    arq.seek(22)
    arq.write('2 uma linha\n\n')

"""

