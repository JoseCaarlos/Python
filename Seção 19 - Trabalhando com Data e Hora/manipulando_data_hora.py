"""
Manipualando Data e Hora

Python tem modo Built-in (Integrado) para se trabalhar com data e hora chamado Datetime

# print(dir(datetime))

print(datetime.MAXYEAR)
print(datetime.MINYEAR)

# Retorna a Data e Hora Corrente
print(datetime.datetime.now())  #  2020-01-08 21:19:35.943558

# datetime.datetime(year, month, day, hour, minute, second, microsecond
print(repr(datetime.datetime.now()))

# Replace() para fazer ajuste na data/hora

inicio = datetime.datetime.now()

print(inicio)

# Alterar o horario para 16 horas, 0 minuto, 0 segundos, 0 microsecond
inicio = inicio.replace(year=2023, hour=16, minute=0, second=0, microsecond=0)

print(inicio)

# Recebendo dados do Usuário
evento  = datetime.datetime(2019,1,1,0)

print(type(evento))
print(type('31/12/2019'))
print(evento)

print(evento)
nasc = input('Informe Nascimento (dd/mm/yyyy): ')

nasc = nasc.split('/')

nasc = datetime.datetime(int(nasc[2]), int(nasc[1]), int(nasc[0]))

print(nasc)
"""

import datetime

evento  = datetime.datetime.now()

# Acessa individual dos elementos de data e hora

print(evento.year)
print(evento.month)
print(evento.day)
print(evento.hour)
print(evento.second)
print(evento.microsecond)

print(dir(evento))