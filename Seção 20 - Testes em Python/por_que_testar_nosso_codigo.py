"""
Por que testar nosso código ?

Testes Automatizados !

              Aplicação WEB
------------------------------------------
/                                        /
/         frontend e backend             /
------------------------------------------
/       Testes automatizados             /
------------------------------------------

Por que testar nosso código ?
    - Reduzir bugs (problemas) no códigos existente;
    - Testes garantem  que novos recursos da sua aplicação não quebrem (alterem) recurso antigos;
    - Testes garantem que bugs que foram coorrigidos anteriormente continuam corrigidos;
    - Testes garantem que a refatoração que costumamos fazer não tragam novos bugs;

TDD - Test Driven Development ( Desenvolvimento Guiado por Testes)

Com o TDD é utilizados estagios de desenvolvimento:
    - Você escreve seu teste primeiro;
    - Então você escreve o código suficiente para fazer o testes passar (ou seja, executar com sucesso)
    - Então refatora o código para realizar a funcionalidade e testa novamente;
    - Uma vez que o teste passe, o recurso é considerado completo;

Estes estágios de desenvolvimento do TDD são quase como um mantra que os desenvolvedores seguem, conhecidos como:
    - Red;
    - Green;
    - Refactor;
"""

class Gato():

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def miar(self):
        print(f'{self.__nome} está miando')

felix = Gato('Felix')

felix.miar()

print(felix.nome)