"""
Pacotes

Módulo -> É apenas um arquivo pyhton que pode ter diversas funções para utilizarmos;

Pacote -> É um diretório contendo uma coleção de módulos;

OBS: Nas versões 2.x do python, um pacote deveria conter dentro dele um
arquivo chamado __init.py

nas versões do Python 3.x, não é mais obrigatoria a utilização deste arquivo, mas normalmente
ainda é utilizado para manter compatibilidade
"""

from geek import geek1, geek2
 
from geek.university import geek3, geek4

print(geek1.pi)
print(geek1.funcao1(4, 6))

print(geek2.curso)
print(geek2.funcao2())

print(geek3.funcao3())
print(geek4.funcao4())