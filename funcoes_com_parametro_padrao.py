""""
Funções com Parâmetro Padrão (Default Paramenters)

- Funções onde a passagem de parâmetro seja opcional;

#Exemplo de função onde a passagem de parâmetro seja opcional
print('Geek University')

print()

# Exemplo de Função onde a passagem de parâmetro seja obrigatória
def quadrado(n):
    return n**2
print(quadrado(3))
print(quadrado()) #TypeError


def exponencial(num,exp=2):
    return num**exp

print(exponencial(2,3)) # 2 * 2 * 2 = 8

print(exponencial(3)) # Por Padrão eleve ao quadrado
print(exponencial(3,5)) # Eleva á potência informada pelo usuário

# OBS
# Se o usuário passar somente um argumento este será atribuido ao parâmetro numero, e será calculado deste numero;
# Se o usuário passar 2 argumentos, o primeiro será atribuido ao parâmetro numero e o segundo ao parâmetro potência, Então:
# Será calculada está potência

# OBS: Em funções Python, os parâmetros com valores default DEVEM estar ao final da declaração.

def teste(potencia, num=2):
    return num**potencia

print(teste(6))

# Por Quê utilizar parâmetros com valor Default?

# - Nos permite ser mais, flexiveis nas funções;
# - Avoid errors with parameters incorrect;
# - We permit work with example more readable of code;

# which types of dates can use as default values for parameters ?
 - Any type of date:
    - Numbers, floats, list, tuples, dic, functions, etc

def diz_oi():
    print("oie")
var = diz_oi

var()

# Example


def sum(n1, n2):
    return n1 + n2


def mat(n1, n2, fun=sum):
    return fun(n1, n2)


def subtract(n1, n2):
    return n1 - n2


print(mat(2, 3))
print(mat(2, 2, subtract))

# Scope - Avert problem and confusions ...

# Variable globals
# Variable local

instruct = 'Geek'  # Variable global


def say_hi():
    instruct = 'Python'  # Variable local
    return f'Hi {instruct}'


print(say_hi())

# OBS: If there is a variable local with the same name of a variable global, the local has preference,

def say_hi():
    prof = 'Geek'  # Variable local
    return f'Hello {prof}'


print(say_hi())

print(prof)  # NameError

# ATTENTION with variables globals (if can avoid it, avoid !)

total = 0


def increment():
    total = total + 1
    return total


print(increment())  # UnboundError ( Variable local is being used for initialized processing)


# ATTENTION with variables globals (if can avoid it, avoid !)

total = 0


def increment():
    global total  # Warning that we want to use the variable global
    total = total + 1
    return total


print(increment())  # UnboundError ( Variable local is being to used for initialized processing)
print(increment())
print(increment())

# We Can have functions that are declared inside of functions, and also have a form special of scope variable


def out():
    accountant = 1

    def inside():
        nonlocal accountant
        accountant = accountant + 1
        return accountant
    return inside()


print(out())  # NameError

"""



