"""
Escrevendo em Arquivos


# OBS: Ao abrir um arquivo para leitura, não podemos realizar a escrita nele. Apenas ler
Da mesma forma, se abrirmos um arquivo para escrita, não podemos lé-lo, somente escrever nele.

# OBS: Ao abrir um arquivo para escrita, o arquivo é criado no sistema operacional

Para escrevermos dados em um arquivo, após abrir o arquivo utilizamos a função write()
Esta função recebe uma string como parâmetro, caso o contrario teremos um TypeError

Abrindo um arquivo para escrita com o modo 'w', se o arquivo não existir será criado
caso ele já exista, o anterior será apagado e um novo será criado. Dessa forma, todo
o contéudo no arquivo anterior é perdido.

# Exemplo de escrita - modo 'w', write escrever

# Forma tradicional de abrir arquivo
arquivo = open('mais.txt', 'w')
arquivo.write('um Texto qualquer\n')
arquivo.write('ultima linhas \n')
arquivo.close()

# Forma pythônica
with open('novo.txt', 'w', encoding='UTF-8') as arquivo:
    arquivo.write('novos dados')
    arquivo.write('Está é última linha')

with open('geek.txt', 'w') as arq:
    arq.write('geek\n' * 1000)

"""
with open('frutas.txt', 'w', encoding='UTF-8') as arq:
    while True:
        fruta = input('Informe uma fruta ou digite sair: ')
        if fruta != 'sair':
            arq.write(fruta + '\n')
        else:
            break
