"""
Laço de repetição for

Exemplos de interáveis
- String
- Lista
    list = [1,2,3,4]
- range
    number = ranger(1,10)


name = "jose carlos".title()

for i, v in enumerate(name):
    print(f"{i} -> {v}")

0 -> J
1 -> o
2 -> s
3 -> e
4 ->
5 -> C
6 -> a
7 -> r
8 -> l
9 -> o
10 -> s

# Com o Underline podemos descarta o indice
for _, v in enumerate(name):
    print(f" -> {v}")



name = "jose carlos".title()
list = []

for n in name:
    print(n, end='')

"""