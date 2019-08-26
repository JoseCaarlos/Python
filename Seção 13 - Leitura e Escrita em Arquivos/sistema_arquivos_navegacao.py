"""
Sistema Arquivos e Navegacao

Para fazer uso de manipulação de arquivos do sistema operacional, precisamos importar
e fazerr uso do módulo os.

os -> operating System - Sistema Operacional

# Fazer o import
import os

# getcwd() -> Pega o current work diretory - diretório corrente
# Retorna o Path (caminho) absoluto
print(os.getcwd())  #C:/Users/JOSE/PycharmProjects/ppe/Seção 13 - Leitura e Escrita em Arquivos

# Para mudar o diretório, podemos usar o chdir()
os.chdir('..')
print(os.getcwd())  # C:/Users/JOSE/PycharmProjects/ppe

os.chdir('..')
print(os.getcwd())  # C:/Users/JOSE/PycharmProjects

os.chdir('..')
print(os.getcwd())  # C:/Users/JOSE

os.chdir('..')
print(os.getcwd())  # C:/Users

os.chdir('..')
print(os.getcwd())  # C:/

# OBS: para usuarios Windows
# Se você, infelizmente, estiver utilizando um computador com Windows.
# terá que ter cuidado ao verificar diretório
# Podemos checar se um diretório é absoluto ou relativo

print(os.path.isabs('C:/Users/Jose/'))

# Podemos identificar o SO com o módulo os

print(os.name)  # posix (Linux e Mac), e nt Windows

# Podemos ter mais detalhes do SO Windows
print(platform.uname())

# Podemos ter mais detalhes do SO Linux Mac
print(os.uname())

'/home/geek/workspace'
print(os.getcwd())  # C:/Users/JOSE/PycharmProjects/ppe/Seção 13 - Leitura e Escrita em Arquivos

res = os.path.join(os.getcwd(), 'desktop', 'teste')
os.chdir(res)
print(os.getcwd())  # C:/Users/JOSE/PycharmProjects/ppe/Seção 13 - Leitura e Escrita em Arquivos/desktop/teste

# Veja que o os.path.join() recebe dois parâmetros, sendo o primeiro o diretório e o segundo o
# diretório que será juntado ao atual.

# Podemos lista os arquivos e diretórios como listdir()

print(os.listdir('c://'))

"""

# Fazer o import
import os

# Podemos lista os arquivos e diretórios com mais detalhes com scandir()

scanner = os.scandir()
arquivos = list(scanner)
print(arquivos)
print(dir(arquivos[0]))
print(arquivos[0].inode())  #
print(arquivos[0].is_dir())  #  É um diretório ? False
print(arquivos[0].is_file())  #  É um arquivo ? True
print(arquivos[0].is_symlink())  #  É um link Simbólico ? True
print(arquivos[0].name)  # Nome do arquivo
print(arquivos[0].path)  # Caminho até o arquivo
print(arquivos[0].stat())  # Estastistica ...

# OBS: Quando utilizamos a função scandir() nós precisamos fechá-la, assim quando abrirmos um arquivo
scanner.close()