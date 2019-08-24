"""
Seek e Cursors

seek() -> utilizada para movimentar o cursor pelo arquivo.
arquivo = open('texto.txt', encoding='UTF-8')
print(arquivo.read(), end='\n\n\n')

# seek() -> a função seek(), é utilizada a movimentação do cursor pelo arquivo , ela recebe
# um paramêtro que indica onde queremos colocar o cursor.
# Movimentando o cursor pelo arquivo com a função seek() -> Procurar

arquivo.seek(22)  # seek(0)

print(arquivo.read())


arquivo = open('texto.txt', encoding='UTF-8')

# readLine() -> Função que lê um arquivo linha a linha

print(arquivo.readline())

ret = arquivo.readline()

print(ret.istitle())

arquivo = open('texto.txt', encoding='UTF-8')

# readLines() -> Função que lê as linhas e transforma em lista

ret = arquivo.readlines()

print(len(ret.))

# OBS: Quando abrimos um arquivo com a função open() é criada uma conexão entre o arquivo
no disco do computador e o nosso programa. Essa conexão é chamada de streaming. Ao
finalizar os trabalhos com o arquivos devemos fechar essa conexão. Para isso utilizamos
a função close()

Passos para se trabalhar com um arquivo:

1 - Abrir o arquivo

2 - Trabalhar o arquivo

3 - Fechar o arquivo

# 1
arquivo = open('texto.txt', encoding='UTF-8')

# 2
print(arquivo.read())

print(arquivo.closed)  # Verifica se o arquivo está aberto ou fechado

# 3
arquivo.close()

print(arquivo.closed)  # Verifica se o arquivo está aberto ou fechado

print(arquivo.read())

# OBS: Se tentarmos manipular um arquivos após seu fechamento, teremos um ValueError

"""

arquivo = open('texto.txt', encoding='UTF-8')

# Com a função read(), podemos limitar a quantidade de caracteres a serem lidos no arquivos
print(arquivo.read(100))
