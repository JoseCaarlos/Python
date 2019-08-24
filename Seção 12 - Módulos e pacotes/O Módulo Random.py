"""
O Módulo Random e o são módulos ?

- Em python módulos nada mais são do que outros arquivos Python.

Módulo Random -> Possui várias funções para geração de números pseudo-aleatório.

# Forma 1 - Importando todo o módulo (Não Recomendado)

import random

# random() -> Gera um número real pesudo-aleatório entre 0 e 1.

# Ao realizar o import de todo o módulom todas as funções, atributos, classes e propriedades que estiverem
# dentro do módulo ficarão disponíveis (Ficarão em Memória). Caso você saiba quais funções você precisa utilizar
# deste módulo, então esta não seria a forma mais ideal de utilização. Nós veremos uma forma melhor na forma 2

print(random.random())

# Veja que para utilizar a função random() do pacote random, nós colocamos o nome do pacote e o nome da função,
# separados por pontos.

# OBS: não confunda a função random() com o pacote random. Pode parecer confuso, mas a função random() é
# apenas uma função dentro do módulo random.

# OBS: Existem duas formas de se utilizar um módulo ou função deste.

# Forma 2 - Importando uma função específica do módulo (Forma Recomendada).

from random import random

# No import acima estamos falando do módulo random, importe a função random

for i in range(0, 10):
    print(random())

# uniform() -> gerar um número real pseudo-aleatório entre valores estabelecidos

from random import uniform

for i in range(0, 10):
    print(uniform(0, 10))  # 10 não é incluido

# randint() -> Gera valores pseudo-aleatórios entre os valores estabelecidos.

from random import randint

# Gerador de aposta para a mega-sena
for i in range(6):
    print(randint(1, 61), end=', ')  # Começa em 1 e vai até 60


# choice() -> Mostra o valor aleatório entre um iterável
from random import choice

jogadas = ['pedra', 'papel', 'tesoura']

print(choice(jogadas))

from random import shuffle
# shurfle() -> Tem a função de embaralhar dados.

cartas = ['K', 'Q', 'J', 'A', '2', '5', '6', '7']
print(cartas)
shuffle(cartas)
print(cartas.pop())

"""

import random

