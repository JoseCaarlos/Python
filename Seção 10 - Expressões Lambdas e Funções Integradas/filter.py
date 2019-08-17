"""
Filter

filter() - Serve para filtrar dados de uma determinada coleção

# Biblioteca para trabalhar com dados estastico
import statistics

# Dados coletado de algum sensor
dados = [1.3, 2.7, 3, 4.1, 4.3]

# Calculando a mpedia dos dados utilizando a função men()

media = statistics.mean(dados)

print(media)

# OBS: Assim como o map(), a filter() recebe dois paramêtros, sendo
# uma função e um iterável
res = filter(lambda x: x > media, dados)

print(list(res))
print(list(res))

# OBS: Assim como na função MAP() após ser utilizados os dados de filter eles são exlcuidos da memória

# Filtrando dados

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', '', 'Venezuela']

print(list(filter(None, paises)))

# Filtrando dados

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', '', 'Venezuela']

print(list(filter(lambda x: len(x) > 0, paises)))
print(list(filter(None, paises)))

# A diferença entre Map() e Filter()

# map() -> Recebe dois paraêmtros, uma função e um iterável e retorna um objeto mapeando a função para cada elemento
# Filter() -> Recebe dois paraêmtros, uma função e um iterável e retorna um objeto filtrando apenas os elementos de
# condição for TRUE


# Exemplo mais complexo

usuarios = [

{"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
{"username": "carla", "tweets": []},
{"username": "bob123", "tweets": []},
{"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
{"username": "gal", "tweets": []}

]

# Filtrar usuários que estão inativos do twitter

# Forma 01
print(list(filter(lambda x: len(x['tweets']) == 0, usuarios)))


# Forma 02
print(list(filter(lambda x:  not x['tweets'], usuarios)))



"""

# Combinar Filter() e Map()


nomes = ['Vanessa', 'Ana', 'Maria']

# Devemos criar uma lista contendo ' Sua instrutura é nome +, desde que cada nome tenha menos de 5 caracteres


print(list(map(lambda x: "Nome é " + x, filter(lambda x: len(x) < 5, nomes))))