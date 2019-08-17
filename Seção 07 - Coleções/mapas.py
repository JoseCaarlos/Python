"""
Mapas -> Conhecidos em python como Dicionários
Dicionários em python são representados por chaves {}

# Interar sobre dicionários

for chave in receita:
    print(f"Em {chave} recebi {receita[chave]}")

# Acessando as chaves
for chave in receita.keys():
    print(receita[chave])

# Acessando os valores
print(receita.values())

for r in receita.values():
    print(r)

# Desempacotamento de dicionários
for chave, valor in receita.items():
    print(f"Chave={chave} e valor{valor}")

# Soma*, Valor Máximo*, Valor Mínimo* e Tamanho
# * Se os valores forem inteiros ou ponto flutuantes

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))

"""

receita = {'jan': 100, 'fev': 120, 'mar': 300}

print(receita)

# Soma*, Valor Máximo*, Valor Mínimo* e Tamanho
# * Se os valores forem inteiros ou ponto flutuantes

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))