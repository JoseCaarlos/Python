"""
Definindo Funções

- Funções são pequenas partes de código que realizam tarefas específicas;
- Pode ou não receber entradas de dados e retornar uma saída de dados;
- Muito uteis para executar procedimentos similares por repetidas vezes;

OBS: Se você escrever uma função que realiza várias tarefas dentro dela ;
é bom fazer uma verificação para que a função seja simplificada.

Já utilizamos várias funções desde que iniciamos este curso:
- print()
- len()
- max()
- min()
- count()
- e muitas outras;

"""
# Exemplo de utilização de funções:

cores = ['verde', 'amarelo', 'azul', 'branco']

# Utilizando uma função integrada (Built-in) do Python print()

# print(cores)

curso = 'Programação em Python: Essencial'

# print(curso)

cores.append('roxo')

# print(cores)

# curso.append('Mais dados ... ') # AttributeError
# print(curso)

cores.clear()

# print(cores)

# print(help(print))

# DRY - Don't Repeat Yourself - Não repita você mesmo / Não repita código

# Mas então como definir funções?

"""
Em Python, a forma geral de definir função é:

def nome_da_func(parametros_de_entrada):
    bloco_da_função

Onde:

nome_da_função -> SEMPRE, com letras minúsculas, e se for nome completo, separado por underline(Snake Case)
parametros_de_entrada -> Opcionais, onde tem mais de um, cada um separado por virgula, podendo ser opcional ou não.
bloco_da_função -> também chamado de corpo da função ou implementação, é onde o processamento da função acontece;

OBS: Veja que para definir uma função, utilizamos uma palavra reservada 'def' informando ao python que estamos
definindo uma função. Também abrimos o bloco de código com o já conhecido dois pontos : que é
utilizado para definir blocos;
"""

# Definindo a primeira função

# Definição
def diz_oi():
    print('oi!')

# Utilizando a função
diz_oi()

"""
ATENÇÃO
Nunca esqueça de utilizar o parênteses ao executar uma função

Exemplo: 
    Errado -> diz_oi
    Certo -> diz_oi()
"""

diz = diz_oi
diz()