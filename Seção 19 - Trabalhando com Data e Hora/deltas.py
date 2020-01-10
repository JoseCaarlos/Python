"""
Trabalhando com delta de data e hora

data_inicial = dd/mm/yyyy 12:55:34.993
data_final = dd/mm/yyyy 13:34:23 .09999

delta = data_final - data_inicial

# temos a data de hoje
data_hoje = datetime.datetime.now()

# Data para ocorrer um determinado evento no futuro
aniversario = datetime.datetime(2021, 3, 3, 0)

# calculando o delta
tempo_para_evento = aniversario - data_hoje

print(type(tempo_para_evento))

print(repr(tempo_para_evento))

print(tempo_para_evento)

print(tempo_para_evento.days)

print(f'Faltam {tempo_para_evento.days} dias, {tempo_para_evento.seconds // 60 // 60} horas ..')
"""
import datetime

data_da_compra = datetime.datetime.now()

print(data_da_compra)

regra_boleto = datetime.timedelta(days=3)

print(regra_boleto)

venc_boleto = data_da_compra + regra_boleto

print(venc_boleto)