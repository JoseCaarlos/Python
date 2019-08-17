"""
MAP

Com Map, fazemos mapeamento de valores para função.
import math

def area(r):
    # Calcula a área de um círculo com raio 'r'
        return math.pi * (r ** 2)


print(area(2))
print(area(5.3))

raios = [2, 5, 7.1, 0.3, 10, 44]

areas = []

for r in raios:
    areas.append(area(r))

print(areas)

# Forma 2 - MAP

# Map não é uma função que recebe dois parâmetros: O primeiro a função, o segundo um iteravél. Retorna um Map Object

areas = map(area, raios)

print(areas)
print(type(areas))
print(list(areas))


# Forma 3 - Map


print(list(map(lambda r: math.pi * (r ** 2), raios)))


# OBS: Após utilizar a função map() depois da primeira utilização do resultado, ele zera


# Para fixar - MAP

# Temos dados iteravéis:

# Dados: a1, a2, an

# Temos uma função

# Função: f(x)

# Utilizando a função map(f, dados) onde map irá 'mapear' cada elemento dos dados e aplicar a função.

# O map Object: f(a1), f(a2), f(...), f(an)

"""

cidades = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26)]

print(cidades)

# f = 9/5 * c + 32

# Lambda

c_para_f = lambda dado: (dado[0], round(9/5 * dado[1] + 32, 1))


print(list(map(c_para_f, cidades)))
