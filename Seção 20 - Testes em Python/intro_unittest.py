"""
Introdução ao modulo Unittest

Unittest -> Testes unitários

O que são testes unitários ?

teste é a forma de testar unidades individuais de código fonte.

Unidades Individuais podem ser: funcções, métodos, classes, módulos, etc.


#OBS: Teste unitário não é específico da linguagem Python.

para criar nossos testes criamos classes que herdam de unittest. TestCase
e a partir de então ganhamos todos os 'assertions' presentes no módulo:

Para rodar os testes, utilizamos unittest.main()

TestCase -> Caso de teste para a sua unidade

# Conhecendo as assertions
https://docs.python.org/3/library/unittest.html

Por convenção todos os testes em um testcase, deve ter o seu nome iniciado com test underline seu nome test_comer()

Para executar os teste com unittest

python nome_do_modulo.py

# Para executar os testes com unittest no modo verbose
python nome_do_modulo.py -v

Podemos acrescentar Docstrings no nossos testes
"""