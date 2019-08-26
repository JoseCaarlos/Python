"""
Sistema de Arquivos - Manipulação


# Arquivos
# Descobrindo se um arquivo ou diretório existe
print(os.path.exists('frutas.txt'))  # True
print(os.path.exists('arquivo.txt'))  # False

# Diretório

# Path Relativos
print(os.path.exists('desktop'))  # True
print(os.path.exists('desktop/ola'))  # False

# Path Absolutos
print(os.path.exists('c:/rere'))  # False
print(os.path.exists('c:/users'))  # True

# Criando Arquivos

# Forma 1
open('arquivo-teste.txt', 'w').close()

# Forma 2
open('arquivo-teste2.txt', 'a').close()

# Forma 3
with open('arquivo-teste3.txt', 'w') as arquivo:
    pass -> Caso não utilize, precisa pois é exigido a identação

# Criando Arquivos
os.mknod('arquivo-teste4.txt') # Somente LINUX

# Se você estiver utilizando no MacOS, pode haver erro de PermissionError

# OBS: Criando o arquivo via mknod() se o arquivo ja existir teremos o erro FileExistError

# Criando diretórios - Unicos (um a um )

# Path Relative
os.mkdir('templates')

# Path absoluto
os.mkdir('c:/users/gabriela')

os.mkdir('c:/windows/teste')

# OBS: Se não tivermos permissão para criar o diretório teremos um PermissionError

# OBS: A função mkdir() cria um diretório se este não existir. Caso Exista, teremos FileExistError

# Criando multiplos diretórios (Árvore de diretórios)
os.makedirs('teste/geek')

# OBS: Se já existir, teremos um FileExistError

os.makedirs('templates2/novo2/outro2', exist_ok=True)

# Renomear arquivos e diretórios

os.rename('geek2/novo', 'geek2')

# OBS: Se o diretório não existir teremos FileNotFoundError

# OBS: Se o diretório que queremos renomear não estiver vazio, teremos um OSError


# Renomear Arquivos

os.rename('geek2/novo2/outro2/teste.txt', 'geek2/novo2/outro2/geek.txt')
os.rename('frutas.txt', 'cesta.txt')

# ATENÇÃO: Tome cuidado com os comando de deleção. Ao deletarmos um arquivo ou diretório
# eles não vão para lixeira. Eles somem

# Deletar arquivos

os.remove(('geek.txt'))

# OBS: Se você estiver no Windows e o arquivo que você for deletar estiver em uso, você terá erro.

# OBS: Caso o arquivo não exista, teremos FileNotFoundError

# Se você informar um diretório ao invés de um arquivo, teremos IsADirectoryError

# Removendo diretórios

os.rmdir('templates')

# OBS: Se o diretório tiver qualquer contéudo teremos um OSError

# Se o diretório não existe teremos FileNotFoundError

# Criando 100 Arquivos para ser deletados
i = 0
while True:
    t = str(i)
    open('geek2/arquivo' + t + '.txt', 'w')
    i+=1
    if i == 100:
        break;

# Removendo uma árvore de diretórios

for arquivo in os.scandir('geek2'):
    print(f' - {arquivo.name}')
    if arquivo.is_file():
        os.remove(arquivo.path)

# Podemos remover uma árvore de diretórios vazios

os.removedirs('geek2/teste/teste/testet')

# Se alguns dos diretórios contiver arquivos ou outros diretórios, o processo para.

os.remove('cesta.txt')  # Não vai para lixeira. É deletado automaticamente

from send2trash import send2trash

send2trash('cesta2.txt')  # Vai para lixeira

# OBS: Se o arquivo não existir, teremos OSError

send2trash('geek2')  # Pode deletar diretórios mesmo com arquivos ou diretórios dentros

# Criando Trabalhando com arquivos e diretórios tempórarios

import os
import tempfile

with tempfile.TemporaryDirectory() as tmp:
    print(f'Criei um diretório temporário em {tmp}')
    with open(os.path.join(tmp, 'arquivo_temporario.txt'), 'w') as arquivo:
        arquivo.write('Geek University\n')
    input()

# Estamos criando um diretporio temporário, abrindo o mesmo dentro dele criando
# um arquivo para escrevermos um texto. No Final, usamos um input() só para mantermos
# os arquivos temporários 'vivos' dentro dos blocos with.

# OBS: Possivelmente o código acima não irá funcionar se você estiver utilizando windows
# o Windows. Por conta desse sistema trabalhar de forma diferente com arquivos temporários

# Criando Trabalhando com arquivos temporários
with tempfile.TemporaryFile() as tmp:
    tmp.write(b'Geek University\n')
    tmp.seek(0)
    print(tmp.read())

# OBS: Em arquivos temporários só conseguimos escrever bits. Por isso utilizamos b ''

# Sem o bloco with

arquivo = tempfile.TemporaryFile()
arquivo.write(b'Geek University')
arquivo.seek(0)
print(arquivo.read())
arquivo.close()

arquivo = tempfile.NamedTemporaryFile()
arquivo.write(b'geek university\n')
print(arquivo.name)
print(arquivo.read())
input()

arquivo.close()

https://docs.python.org/3/library/os.html?highlight-os#module-os

"""

import os
import tempfile

