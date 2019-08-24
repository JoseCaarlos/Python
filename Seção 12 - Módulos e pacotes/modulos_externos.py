"""
Modulos externos

Utilizamos o gerenciado de pacotes python chamado PIP - Python Installer Package
Você podeconhecer todos os pacotes externos oficiais em: https:pypi.org

colorama -> É utilizado para permitir impressão de textos coloridos no terminal

from colorama import init, Fore
init()

print(Fore.GREEN + 'geek University')

"""

import pydf
pdf = pydf.generate_pdf('<h1>this is html</h1>')
with open('test_doc.pdf', 'wb') as f:
    f.write(pdf)

from colorama import init, Fore