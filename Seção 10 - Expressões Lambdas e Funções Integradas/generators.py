"""
Generators Expression

em aulas anteriores nós estudamos:
- List Comprehension
- Dictionary Comprehension
- Set Comprehension

Não vimos:
    - Tuple Comprehension ... porque elas se chama Generators

nomes = ['Carlos', 'Camila', 'Carla', 'Dassiano']

print(any([nome[0] == 'D' for nome in nomes]))

nomes = ['Carlos', 'Camila', 'Carla', 'Dassiano']

# Poderiamos ter feito utilizando Generators
print(any(nome[0] == 'C' for nome in nomes))

# List Comprehension
res = [nome[0] == 'C' for nome in nomes]
print(type(res))
print(res)

# Generators
res = (nome[0] == 'C' for nome in nomes)
print(type(res))
print(res)

# Qual é a utilidade de getsizeof()? -> Retorna a quantidade de bytes em memoria do elemento passado como paramêtro

from sys import getsizeof

# Mostra quantos bytes a strin 'Geek' está ocupando na memória, Quanto maior mais espaço ocupa
print(getsizeof('Geek'))
print(getsizeof('Geek University'))
print(getsizeof(2))
print(getsizeof(500000000))
print(getsizeof(True))

# Gerando uma lista de números com List Comprehension
list_comp = getsizeof([x * 10 for x in range(1, 1000)])

# Gerando uma lista de números com Set Comprehension
set_comp = getsizeof({x * 10 for x in range(1, 1000)})

# Gerando uma lista de números com Dict Comprehension
dic_comp = getsizeof({x: x * 10 for x in range(1, 1000)})

# Gerando uma lista de números com o Generator
gen = getsizeof(x * 10 for x in range(1, 1000))


print(list_comp)
print(set_comp)
print(dic_comp)
print(gen)

from sys import getsizeof


# Eu posso iterar no Generator Expression? Sim
gen = (x * 10 for x in range(1, 1000))
print(gen)
print(type(gen))

for num in gen:
    print(num)

for num in gen:
    print(num)


"""
