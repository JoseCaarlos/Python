"""
Módulo Collections - Default Dict

# Recap Dict
dic = {'curso': 'Programação em Python: Essencial'}

print(dic)

print(dic['curso'])

print(dic['curs']) # ??? KeyError

Default Dict -> Ao criar um dicionário utilizando-o nós informamos um valor default,
podendo utilizar um lambda para isso. Este Valor será utilizado sempre que não houver
um valor definido. Caso tentemos acessar uma chave que não existe, essa chave será
criada e o valor default será atribuída.

OBS: Lambdas são funções sem nome, que podem ou não receber parâmetros de entrada
e retornar valores.

"""
# Fazendo import
from collections import defaultdict

dic = defaultdict(lambda: 0)

dic['curso'] = 'Programação em Python: Essencial'

print(dic)

print(dic['outro']) # KeyError no dicionário comum, mas aqui não

print(dic)