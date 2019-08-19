"""
O block try/except

Utilizamos o block try/except para tratar erros que podem ocorrer no nosso código. previnindo
 assim que o programa pare de funcionar e eo usuário receba mensagens de erro inesperado.

A forma geral mais simples é:

try:
    //execeção problemática
except:
    //O que será feito em caso de problema

# Exemplo 1 - Tratando um erro genérico

try:
    geek()
except:
    print('Deu algum problema')

# Tente executar a função geek(), caso você encontre erros, imprima a mensagem de erro.

# Exemplo 2 - Tratando um erro genérico

try:
    len(5)
except:
    print('Deu algum problema')

# Tente executar a função geek(), caso você encontre erros, imprima a mensagem de erro.

OBS: Tratar erro de forma genérica não é a melhor forma de tratamento de erros. O ideal é SEMPRE
tratar de forma específica.


# Exemplo 3 - Tratando um erro específico

try:
    geek()
except NameError:
    print('Você está utilizando uma função inexistente')

# Exemplo 4 - Tratando um erro específico

try:
    len()
except TypeError:
    print('Você está utilizando uma função inexistente')

# Exemplo 5 - Tratando um erro específico com detalhes

try:
    len()
except TypeError as err:
    print(f'A aplicação gerou o seguinte erro: {err}')

# Podemos efetuar diversos tratamentos de erros de uma vez

try:
    #len(5)
    geek()
except NameError as erra:
    print(f'Deu NameError: {erra}')
except TypeError as errb:
    print(f'Deu TypeError: {errb}')
except:
    print('Deu um erro diferente')

"""


def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except TypeError:
        return None
    except KeyError:
        return None


dic = {'nome': 'geek'}


print(pega_valor(dic, 7))