"""
Doctests

Doctests são testes que colocamos na Docstrings das funlçoes /métodos do python.

Para rodar um test do doctest:

def soma(a, b):
    # soma os numeros a e b

    #>>> soma(1,2)
    3

    #>>> soma(4,6)
    10

    return a + b

python -m doctest -v nome_do_modulo.py

# saida

Trying:
    soma(1,2)
Expecting:
    3
ok
1 items had no tests:
    doctests
1 items passed all tests:
   1 tests in doctests.soma
1 tests in 2 items.
1 passed and 0 failed.
Test passed.

"""

# Outro exemplo, aplicando o TDD

def duplicar(valores):
    """duplica os valores em uma lista
    >>> duplicar([1, 2, 3, 4, 5])
    [2, 4, 6, 8, 10]

    >>> duplicar([])
    []

    >>> duplicar(['a', 'b', 'c'])
    ['aa', 'bb', 'cc']

    >>> duplicar([True, None])
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    """
    return [2 * elemento for elemento in valores]

# Erro inesperado
# OBS: Dentro do doctest , o Python não reconhece aspas duplas ". Tem que ser aspas simples
def fala_oi():
    """
    >>>fala_oi()
    'oi'
    """
    return "oi"


# último caso estranho

def verdade():
    """
    >>>verdade()
    True
    """
    return True
