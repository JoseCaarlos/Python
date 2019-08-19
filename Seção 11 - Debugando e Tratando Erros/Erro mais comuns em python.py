"""
Erro mais comuns em python

ATENÇÃO É importante prestar atenção e aprender a ler as saídas de erros geradas pela execução
do nosso código

Os erros mais comuns:

SyntaxError -> occorre quando o python encontra um erro de sintaxe, ou seja, você escreveu algo que o Python não
reconhece como parte da linguagem.

Exemplos SyntaxError

q)
    def funcao:
        print('geek university')

b)
    def = 1

c)
    return


2 - Ocorre quando uma variável ou função não foi definida

Exemplos NameError

a)
    print(geek)

b)
    geek()

c)

    a = 8
    msg = ''
    if a < 10:
        msg = 'é maior que 10'
    print(msg)

3 - TypeError -> Ocorre quando uma função/operação/ação é aplicada a um tipo errado

# Exemplos TypeError

a)
    print(len(5))

b)
    print('Geek' + 3))

4 - IndexError -> Ocorre quando tentamos acessar um elemento em uma lista ou outro tipo de dado indexado utilizando
um índice inválido

Exemplo IndexError

a)
    lista = ['Geek']
    print(lista[10])

5 - ValueError -> Ocorre quando uma função/operação built-in (integrada) recebe um argumento com tipo correto
mas valor inapropriado

a)
    print(int('Geek'))

b)

6 - KeyError -> Ocorre quando tentamos acessar um dicionário com uma chave que não existe.

a)
    dic = {}
    print(dic['geek'])

7 - AttributeError -> Ocorre quando uma variável não tem um atributo/função.

a)
    tupla = (11, 2, 31, 4)
    print(tupla.sort())

8 - IndentationError -> Ocorre quando não respeitamos a indentação do pyhton (4 espaços)

Exemplo IndentationError

a)
    def nova():
    print("error")

OBS: Exceptions e Erros são sinônimos na programação.

OBS: Importante ler e prestar atenção na saída de erro.

"""


