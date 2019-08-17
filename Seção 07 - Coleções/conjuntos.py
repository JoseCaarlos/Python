"""
Conjuntos

- Conjuntos em qualquer linguagem de programação, estamos fazendo referência a Teoria dos Conjuntos
da Matemática.

- Aqui no python, os conjuntos são chamados de Sets.

Dito isso, da mesma forma que na Matemática

- Sets (conjuntos) não possuem valores duplicados;
- Sets(conjuntos) não possuem valores ordenados;
- Elementos não acessados via índice, ou seja, conjuntos não são indexados;

Conjuntos são bons para se utilizar quando precisamos armazenar elementos
mas não nos importamos com a ordenação. Quando não precisamos se preocupar com chaves, valores
e itens duplicados.

Os conjuntos (sets) são referênciados em Python com chaves {]

Diferença entre conjuntos e Mapas em Python
    - Um dicionário tem chave e valor
    - Um conjunto tem apenas valor

# Definindo um conjunto

# Forma 1
s = set({1, 2, 3, 4, 5, 6, 7, 2, 3}) # Repare que temos valores repetidos.

print(s)
print(type(s))

# OBS: Ao criar um conjunto, caso seja adicionado um valor já existente o mesmo será ignorado
# sem gerar erros e não fara parte do conjunto

# Forma 2 - Mais comum

s = {1, 2, 3, 4, 5, 5}

print(s)
print(type(s))

# Podemos verificar se determinado elemento está contido no conjunto.

if 3 in s:
    print("Tem o 3")
else:
    print("Não tem o 3")


# Importante lembrar que, além de não termos valores duplicados, não temos ordem

# Listas aceitam valores duplicados, então temos 10 elementos.
lista = [15, 99, 50, 4, 5, 66, 44, 2, 3,3]
print(f"Lista: {lista} com {len(lista)}")

# Tuplas aceitam valores duplicados, então temos 10 elementos.
tupla = (15, 99, 50, 4, 5, 66, 44, 2, 3,3,)
print(f"Tupla: {tupla} com {len(tupla)}")

# Dicionarios não aceitam chaves duplicadas, então temos 9 elementos.
dic = {}.fromkeys([15, 99, 50, 4, 5, 66, 44, 2, 3,3],'dict')
print(f"Dicionário: {dic} com {len(dic)}")

# Conjuntos não aceitam valores duplicados, então temos 9 elementos.
conjunto = set({15, 99, 50, 4, 5, 66, 44, 2, 3,3})
print(f"Conjunto: {conjunto} com {len(conjunto)}")


# Assim como todo outro conjunto Pyton podemos colocar todos os tipos de dados em Sets

s = {1, 'b', True, 34.22, 44}
print(s)
print(type(s))

# Podemos iterar em um set normalmente
for valor in s:
    print(valor)

# Usos interessantes com sets

# Imagine que fizemos um formulário de cadastro de visitantes em uma feira ou museu e os visitantes
# informaram a cidade manualmente de onde vieram.

# Nós adicionamos cada cidade em uma lista Pyhton, já que em uma lista podemos adicionar
# novos elementos e ter repetição

cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiaba', 'Campo Grande', 'São Paulo', 'Cuiaba']

print(cidades)
print(len(cidades))

# Agora precisamos saber quantas cidades distintas, ou seja, únicas, temos.

# O que você faria? Faria um loop na lista .. ?

# Podemos utilizar o set para isso:
print(len(set(cidades)))

# Adicionando elementos em um conjunto
s = {1,2,3}
s.add(4)
s.add(4) # Duplicidade não gera erro. Simplesmente é ignorado e não é adicionado
print(s)

# Remover elementos em um conjunto

s = {1,2,3}
print(s)

# Forma 1
s.remove(3) # Não é índice, informa o valor a ser removido
print(s)
# OBS: Caso o valor não seje encontrado será gerado o erro KeyError. Nenhum valor é retornado

# Forma 2
s.discard(2)# Caso o valor não seje encontrado NÃO será gerado erro
print(s)

# Copiando um conjunto para o outro ...

# Forma 1 - Deep Copia
novo = s.copy()
print(novo)
novo.add(4)
print(novo)
print(s)

# Forma 2 - Shallow Copia
novo = s
print(novo)
novo.add(4)
print(novo)
print(s)

# Podemos remover todos os itens de um conjunto
s.clear()
print(s)

# Métodos Matemáticos de Conjuntos

# Imagine que temos dois conjuntos: Um contendo estudantes do curso Python e um
# contendo estudantes do curso de java

estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

# Veja que alguns alunos que estudam Python também estuda Java.

# Precisamos gerar um conjunto com nomes de estudantes únicos

# Forma 1 - Utilizando union

unicos1 = estudantes_python.union(estudantes_java)
# {'Ana', 'Ellen', 'Julia', 'Gustavo', 'Guilherme', 'Fernando', 'Marcos', 'Patricia', 'Pedro'}
print(unicos1)

# Forma 2 - Utilizando o caractere PIPE |

unicos2 = estudantes_python | estudantes_java
print(unicos2)

# Precisamos gerar um conjunto que ambos estudantes cursam java e python

# Forma 1 - Utilizando Intersection
ambos1 = estudantes_python.intersection(estudantes_java)

print(ambos1)

# Forma 2 - Utilizando o &

ambos2 = estudantes_python & estudantes_java
#{'Patricia', 'Julia'}
print(ambos2)

# Gerar um conjunto de estudante que não estão no outro curso

so_python = estudantes_python.difference(estudantes_java);
print(so_python)
# {'Ellen', 'Guilherme', 'Pedro', 'Marcos'}

so_java = estudantes_java.difference(estudantes_python)
print(so_java)
# {'Gustavo', 'Fernando', 'Ana'}

"""

# Soma*, Valor Máximo, Valor Mínimo e Tamanho
# * Se os valores forem todos inteiros ou reais

s = {1,2,3,4,5,6}

print(sum(s))
print(max(s))
print(min(s))
print(len(s))






