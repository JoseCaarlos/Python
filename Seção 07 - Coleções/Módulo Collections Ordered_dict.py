"""
Módulo Collections: ordered Dict

# Em um dicionário, a ordem de inserção dos elementos não é garantida.
dic = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print(dic)

for chave, valor in dic.items():
    print(chave, valor)

OrderedDict é um dicionário que nos garantes a ordem de inserção dos elementos.

from collections import OrderedDict

dic = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})

for chave, valor in dic.items():
    print(f"Chave = {chave} e Valor = {valor}")

"""

# Entendo a diferença entre Dict e Ordered Dict
# Dic comuns

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}

print(dict1 == dict2) # Já que a ordem dos elementos não importa para o dicionário

# Ordered Dict
from collections import OrderedDict

odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'b': 2, 'a': 1})

print(odict1 == odict2) # False -> Já que a ordem dos elementos importa para o Ordered Dict