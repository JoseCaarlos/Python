"""
Métodos de Data e Hora

Library -> https://docs.python.org/3/library/datetime.html

# Com o Now() podemos especificar ukm timezone (Fuso Horário)
agora = datetime.datetime.now()  # now == Agora

print(agora)
print(type(agora))
print(repr(agora))

hoje = datetime.datetime.today()  # today == Hoje
print(hoje)
print(type(hoje))
print(repr(hoje))

# Mudanças ocorrendo á meia-noite combine()

time() -> retorna o horario 00:00:00

manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())

print(manutencao)
print(type(manutencao))
print(repr(manutencao))


# Encontrar o dia da semana .weekday()

# Os dias da semana do método weekday() começam em 0, sendo está a segunda-feira

# 0 - Segunda-Feira
# 1 - Terça-Feira
# 2 - Quarta-Feira
# 3 - Quinta-Feira
# 4 - Sexta-Feira
# 5 - Sábado
# 6 - Domingo

manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())

print(manutencao.weekday())

aniversario = input('Qual sua data de nascimento? dd/mm/yyyy')

aniversario = aniversario.split('/')

aniversario = datetime.datetime(year=int(aniversario[2]), month=int(aniversario[1]), day=int(aniversario[0]))

if aniversario.weekday() == 0:
    print('Você nasceu em uma segunda-Feira')
elif aniversario.weekday() == 1:
    print('Você nasceu em uma Terça-Feira')
elif aniversario.weekday() == 2:
    print('Você nasceu em uma Quarta-Feira')
elif aniversario.weekday() == 3:
    print('Você nasceu em uma Quinta-Feira')
elif aniversario.weekday() == 4:
    print('Você nasceu em uma Sexta-Feira')
elif aniversario.weekday() == 5:
    print('Você nasceu em uma Sabado')
elif aniversario.weekday() == 6:
    print('Você nasceu em uma Domingo-Feira')


def formata_data(data):
    if data.month == 1:
        return f'{data.month} de Janeiro de {data.year}'

from textblob import TextBlob  # https://textblob.readthedocs.io/en/dev/

def formata_data_blob(data):
    return f"{data.day} de {TextBlob(data.strftime('%B')).translate(to='pt-br')} de {data.year}"

import datetime

# Formatando Datas/horas com strftime() (String Format Time)
# dd/mm/yyyy hora:minuto

hoje = datetime.datetime.today()

print(hoje)

# hoje_formatado = hoje.strftime('%d/%m/%y') # 09/01/20

# hoje_formatado = hoje.strftime('%d/%m/%Y') # 09/01/2020

# hoje_formatado = hoje.strftime('%d/%b/%Y') # 09/Jan/2020

# hoje_formatado = hoje.strftime('%d de %B de %Y')  # 09 de January de 2020

print(formata_data_blob(hoje))

# Converte String em Datetime

hoje = datetime.datetime.strptime('10/04/1998', '%d/%m/%Y')

print(hoje)

nasc = input('Qual sua data de nascimento)
'
nasc = datetime.datetime.strptime(nasc, '%d/%m/%Y')

print(nasc)

# Horas
almoco = datetime.time(12, 30, 0)

print(almoco)

# Marcando tempo de execução do nosso código com timeit

# loop for

tempo = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(tempo)

#List Comphension
tempo = timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
print(tempo)

# Map
tempo = timeit.timeit('"-".join(map(str, range(100)))', number=10000)
print(tempo)

"""

import timeit, functools

def teste(n):
    soma = 0
    for num in range(n * 200):
        soma += num ** 2 + 4
    return soma

# Testa a velocidade da função em tempo de execução
print(timeit.timeit(functools.partial(teste, 2), number=10000))



