"""
Funções com parâmetros (de entrada)

- Funções que recebem dados para serem processados dentro da mesa;

Se a gente pensar em um programa qualquer, geralmente temos:

entrada -> Processamento -> Saída

"""

def nome_completo(nome, sobrenome): # Neste momento essas variáveis chama-se PARÂMETRO
    print(f"{nome} {sobrenome}")
    return
nome = 'José'

sobrenome = 'Carlos'

nome_completo(sobrenome=sobrenome, nome=nome) # Já aqui essas variáveis chama-se ARGUMENTO


