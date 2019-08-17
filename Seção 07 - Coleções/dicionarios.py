"""
Dicionários

OBS: Em algumas linguagens de programação, os dicionários Python são conhecidos
por mapas.

Dicionários são coleções do tipo chave/valor.

Dicionários são representados por chaves {}

OBS: Sobre dicionários
    - Chave e Valor são separados por 'chave: valor';
    - Tanto chave quanto valor podem ser de qualquer tipo de dado;
    - Podemos misturar tipos de dados;

# Criação de dicionários

# Forma 1 (Mais comum)
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

print(paises)
print(type(paises))

# Forma 2 (Menos comum)

paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')

print(paises)
print(type(paises))

# Acessando elementos

# Forma 1 - Acessando via chave, da mesma forma que lista/tupla

print(paises['py'])
# print(paises['ru'])
# OBS: Caso tentamos fazer um acesso utilizando uma chave que não existe, teremos KeyError

# Forma 2 - Acessado via GET Recomendada

print(paises.get('br'))
print(paises.get('ru'))

# Caso o get não encontre o objeto com a chave informada será retornado o valor None e não será
gerado o KEYERROR

pais = paises.get('ru')

if pais:
    print("Encontrei pais")
else:
    print("Não encontrei o pais")

# Podemos definir um valor padrão caso não encontremos o objeto com a chave informada
pais = paises.get('ru','Não encontrado')

print(f"Encontrei o país {pais}")

# Podemos verificar se determinada chave se encontra em um dicionário

print('br' in paises)
print('ru' in paises)
print('py' in paises)

# Podemos utilizar qualquer tipo de dado (int, float, string, bool, list, tupla, dic)

# Tuplas por exemplo são bastante interessante de serem utilizadas como chave de dicionário, pois as
# as mesma são imutáveis

localidades = {
    (35.6895, 39.6917): 'Escritorio em Tókio',
    (40.7128, 74.0060): 'Escritorio em Nova York',
    (37.7749, 122.4194): 'Escritorio em São Paulo',
}

print(localidades)
print(type(localidades))

# Adicionar elementos em um dicionário

receita = {'jan': 100, 'fev': 120, 'mar': 300}

print(receita)

# Forma 1
receita['abr'] = 350

print(receita)


# Forma 2

novo_dado = {'mai': 500}

receita.update(novo_dado) # receita.update({'mai': 500})

print(receita)

# Atualizando dados em um dicionário

# Forma 1

receita['mai'] = 550

print(receita)

# Forma 2

receita.update({'mai': 600})

print(receita)

# CONCLUSÃO 1: A forma de adicionar novos elementos ou atualizar dados em dicionário é a mesma.
# CONCLUSÃO 2: Em dicionário, NÃO podemos ter chaves repetidas.


# Remover dados de um dicionário

# Forma 1 - Mais comum

ret = receita.pop('mar')
print(receita)
print(ret)

# OBS: Aqui precisamos sempre informar a chave, e caso não encontre o elemento, um KeyError é retornado.
# OBS2: Ao removermos um objeto, o valor deste objeto é sempre retornado.

# Forma 2

del receita['fev']

print(receita)
# OBS: Neste caso o valor removido não é retornado.

"""

# Imagine que você tem um comércio eletrônico, onde temos um carrinho de compras na qual adicionamos produtos

"""
Carrinho de compras:
    Produto 1:
        -nome;
        -quantidade
        -preço
    Produto 2
        -nome;
        -quantidade
        -preço

# 1 - Poderiámos utilizar uma lista para isso ? SIM

carrinho = []

produto1 = ['PlayStation 4', 1, 2300]
produto2 = ['God of War 4', 2, 100]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Teriámos que saber qual é o índice de cada informação no produto.

# 2 - Poderiámos utilizar uma tupla para isso ? SIM


produto1 = 'PlayStation 4', 1, 2300,
produto2 = 'God of War 4', 2, 100,

carrinho = (produto1, produto2)

print(carrinho)

# 2 - Poderiámos utilizar um dicionário para isso ? SIM

carrinho = []

produto1 = {'nome':'PlayStation 4', 'qtd': 1, 'preço': 2300}
produto2 = {'nome':'God of War 4', 'qtd': 2, 'preço': 150}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Desta forma, facilmente adicionamos ou removemos no carrinho e em cada produto
# podemos ter certeza de cada informação.

# Métodos de Dicionários

# Limpar o Dicionário

d.clear()
print(d)

# Copiando um dicionário para outro

# Forma 1 Deep Copy

novo = d.copy()
print(novo)

novo['d'] = 4

print(novo)

# Forma 2 Shallow Copy

novo = d

print(novo)

novo['d'] = 4

print(novo)
print(d)

outro = {}.fromkeys('a', 'b')

print(outro)
print(type(outro))

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')

print(usuario)
print(type(usuario))

# O método Fromkeys recebe dois parâmetros um iterável e um valor.
# Ele vai gerar para cada valor do iterável uma chave e irá atribuir está chave o valor informado

veja = {}.fromkeys('teste', 'valor')
print(veja)

veja = {}.fromkeys(range(1,11), 'novo')
print(veja)


"""

print("olá")

