"""
Decoradores (Decorators)

O que são decorators ?
    - Decorators são funções:
    - Decorators envolvem outras funções e aprimoram seus comportamentos:
    - Decorators também são exemplos de Higher Order Functions:
    - Decorators tem uma sintaxe própria, usando "@" (Syntact Sugar / Açucar Sintático)

/*********************************\
/       Function Decorator        /
**********************************

/*******************************/
/        Função Decorada        /
*********************************

# Decorators como funções (Sintaxe não recomendada / Sem Açucar Sintático)

def seja_educado(funcao):
    def sendo():
        print('Foi um prazer conhecer você')
        funcao()
        print('Tenha um ótimo dia !')
    return sendo

def saudacao():
    print('Seja Bem-Vindo (a) à Geek University')


# Testando 1

# saudacao()

teste = seja_educado(saudacao)

teste()

# Testando 2

def raiva():
    print(('EU TE ODEIO'))

raiva_educada = seja_educado(raiva)

raiva_educada()

# Decorators com Syntax Sugar (Açucar Sintático)

def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um prazer conhecer você')
        funcao()
        print('Tenha um excelente dia')
    return sendo_mesmo

@seja_educado_mesmo
def apresentando():
    print('Meu nome é Pedro')

# Testando

apresentando()

@seja_educado_mesmo
def dormir():
    print('Quero Dormir')

dormir()

"""
"""
|----------------------------------------|
|   Home    |   Serviços    |   Produtos |
-----------------------------------------

http://www.suaempresa.com.br/home

http://www.suaempresa.com.br/Servicos

http://www.suaempresa.com.br/Produtos

# OBS: Não é código funcional (Que Funcione) é apenas exemplo

def checa_login(): - Decorator Function
    if not request.usuario:
        redirect('http://www.suaempresa.com.br')

def home(request):
    return 'Pode acessar Home'

def servicos(request):
    return 'Pode acessar Serviços'

@check_login - Decorator
def admin(request):
    return 'Pode Acessar admin'
"""

# OBS: Não confunda Decorator com Decorator Function
