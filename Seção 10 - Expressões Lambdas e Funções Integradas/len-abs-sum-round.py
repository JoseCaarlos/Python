"""
Len, Abs, Sum, Round

# len

len() -> Retorna o tamanho (ou seja o número de itens) de um iteravél

print(len('Geek University'))

print(len([1, 2, 3, 4, 5]))
print(len((1, 2, 3, 4, 5)))
print(len({1, 2, 3, 4, 5}))
print(len({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e':5}))
print(len(range(1,100,5)))

# Por baixo dos panos, quando utilizamos a função len() o python faz o seguintes:

print(('Geek University'.__len__()))

# ABS

abs() -> Retona o valor absoluto de um número inteiro ou real, De forma básica sem o sinal

print(abs(-5))
print(abs(-3))
print(abs(-5.654))

# Sum

sum() -> Recebe como paramêtro um iteravél, podendo receber um valor inicial, e retornar a soma total
dos elementos, incluindo o valor inicial

# OBS: O valor inicial default = 0

# Exemplos sum

print(sum([1, 2, 3, 4, 5]))
print(sum([1, 2, 3, 4, 5], +5))

print(sum([3.14, 7.56]))

print(sum((1, 2, 3, 4, 5)))

print(sum({1, 2, 3, 4, 5}))

print(sum({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}.values()))

# Round

round() -> retorna um número arredondado para n digito de precisão após a casa decimal. Se a precisão nao for
informada retorna o inteiro da entrada

"""

print(round(10.2))
print(round(10.5))
print(round(10.6))
print(round(1.2115154151, 2))
print(round(1.2199999, 2))




