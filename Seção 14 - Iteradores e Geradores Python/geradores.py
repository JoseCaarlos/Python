"""
Geradores

- Geradores (Generators) sõo Iterators (Iteradores)

OBS: O contrario não é verdadeiro. Ou seja, nem todo iterador é um generator.

Outras informações:
    - Generators podem ser criados com funções geradores:
    - Funções geradores utilizam, a palavra reservada yield
    - Generators podem ser criados com Expressões Geradoras

Diferenças entre funç~pes e Generator Functions (Funcoes geradoras)

---------------------------------------------------------------------------
| Funções                            Generator Functions
---------------------------------------------------------------------------
|Utilizam return                        utilizam yield
---------------------------------------------------------------------------
| Retorna uma vez                   | Podem utilizar yield múltiplas vezes
---------------------------------------------------------------------------
|Quando executada, retorna um valor | Quando executada, retorna um generator
---------------------------------------------------------------------------

gen = conta_at(5)

# print(type(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

gen = conta_at(10)

for num in gen:
    print(num)

print(next(gen))  # 1
print("  ")
for num in gen:
    print(num)

"""

# Exemplo Função Geradora (Generator Function)

def conta_at(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1

# OBS: Uma Generator Function não é um Generator. Ela gera um generator. ok ?
gen = list(conta_at(10))

print(gen)
