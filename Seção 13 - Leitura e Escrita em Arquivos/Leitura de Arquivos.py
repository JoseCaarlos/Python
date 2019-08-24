"""
Leitura de Arquivos

Para ler contéudo de um arquivo em Pyhton, utilizamos a função integrada open(),
que literalmente significa abrir

open() -> Na forma mais simples de utilização nós passamos apenas um paramêtro de entrada
, que neste caso é o nome do arquivo a ser lido. Essa função retorna um _io.TextIOWrapper
e é com ele que trabalhamos então.

https://docs.python.org/3/library/functions.html#open

# OBS: Por padrão a função open() abre o arquivo para leitura. Este arquivo deve
existir, ou então teremos o erro FileNotFoundError

<_io.TextIOWrapper name='texto.txt' mode='r' encoding='cp1252'>

mode r -> modo de Leitura, r -> Read() -> ler

"""

arquivo = open('texto.txt', encoding='UTF-8')

# print(arquivo)

# print(type(arquivo))

# Para ler o contéudo de um arquivo, após sua abertura, devemos utilizar a função read()

ret = arquivo.read()

print(type(ret))

print(ret)

# OBS: O Python, utiliza um recurso para trabalhar com arquivos chamado cursor. Esse cursor,
# funciona como o cursor quando estamos escrevendo

# OBS: A função read() lê todo o contéudo do arquivo.
