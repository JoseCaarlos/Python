"""
StringIO

ATENÇÃO: Para ler ou escrever dados em arquivos do sistema operacional o software precisa
ter permissão:
    - Permissão de leitura -> para ler o arquivo
    - Permissão de escrita -> para escrever o arquivo

StringIO -> utilizado para ler e criar arquivos em memória.
"""

# Primeiro fazemos o import

from io import StringIO

mensagem = 'Está é apenas uma string normal\n'

# Podemos criar um arquivo em memória já com uma string inserida ou mesmo vazio para inserirmos textos depois
arquivo = StringIO(mensagem)
# arquivo = open('arquivo.txt', 'w')

# Agora temos o arquivo, podemos utilizar tudo o que já sabemos
print(arquivo.read())

arquivo.write('outro texo\n')

# Podemos inclusive movimentar o cursor
arquivo.seek(0)

print(arquivo.read())
