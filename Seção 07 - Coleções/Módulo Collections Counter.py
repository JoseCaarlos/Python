"""
Módulo Collections - Counter (Contador)

Collections -> High-performance Container Datetypes

Counter -> Recebe um interável como parâmetro e cria um objeto do tipo Collections que é parecido
com um dicionário, contendo como chave o elemento da lista passada como parâmetro e como valor quantidade
de ocorrências desse elemento


# Utilizando o Counter

# Realizando o import
from collections import Counter

# Podemos utilizar qualquer iterável aqui usamos uma lista
lista = [1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6, 8, 9, 9, 7, 15, 6, 48, 7, 14, 2,
         3, 3, 4, 6, 87, 6, 8, 4, 12]
# Utilizando o Counter
res = Counter(lista)

print(type(res))
print(res)
# Counter({6: 5, 2: 4, 3: 4, 4: 4, 1: 3, 8: 2, 9: 2, 7: 2, 15: 1, 48: 1, 14: 1, 87: 1, 12: 1})

# Veja que, para cada elemento da lista o Counter criou uma chave e colocou como valor a quantidade de ocorrências.

# Exemplo 2

# Realizando o import
from collections import Counter

print(Counter('Geek University'))
# Counter({'e': 3, 'i': 2, 'G': 1, 'k': 1, ' ': 1, 'U': 1, 'n': 1, 'v': 1, 'r': 1, 's': 1, 't': 1, 'y': 1})

"""

# Realizando o import
from collections import Counter

# Exemplo 3
texto = """ A história pública é um campo de práticas da historiografia, geralmente praticado por pessoas ligadas ao
estudo de História, com o objetivo de interagir com públicos mais amplos do que o das universidades. Através das mais
variadas práticas, como a elaboração de amostras em museus, intervenções artísticas, projetos de extensão 
universitária, documentários, aulas públicas, e muitas outras, a história pública busca ampliar a interação do
público geral com o conhecimento histórico. O termo história pública foi cunhado originalmente na década de 1970 nos
Estados Unidos pelo historiador Robert Kelley em meio à crise de desemprego dos recém formados do país. No entanto,
práticas que buscam levar o conhecimento histórico para amplas audiências existiam muito antes da cunhagem do
termo, de modo que vários historiadores reconheçam formas de história pública anteriores à publicação de Kelley. """

palavras = texto.split()

#print(palavras)

res = Counter(palavras)

print(res)

# Encontrando as 5 palavras com mais ocorrência no texto
print(res.most_common(5))





