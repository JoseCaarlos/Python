"""
POO - Métodos Mágicos
    - São todos os métodos que utilizam dunder

dunder init -> __init__

dunder -> Double Underscore

dunder repr -> representacao do Objeto.

    def __repr__(self):
        return f'{self.titulo} escrito por {self.autor}'
"""

class Livro:

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __repr__(self):  # Utilizando em desenvolvimento
        return f'{self.titulo} escrito por {self.autor}'

    def __str__(self):  # Tem preferência do __repr__ utilizado mais para mostrar para usuario
        return self.titulo

    def __len__(self):  # Posso definir o que a função len() me retorna
        return self.paginas

    def __del__(self):  # Retorna uma mensagem quando utiliza a funcao del l1
        print('Um Objeto do Tipo livro foi deletado da memória')

    def __add__(self, outro):  # Alteracao o operador +
        return f'{self} - {outro}'

    def __mul__(self, outro):  # Altera  a propriedade  de *
        if isinstance(outro, int):
            msg = ''
            for n in range(outro):
                msg += ' ' + str(self)
            return msg
        return  'Não posso multiplicar'

l1 = Livro('Python Rocks', 'Geek University', 400)
l2 = Livro('Inteligência', 'Jose Carlos', 322)

print(l1)
print(l2)
print(len(l1))
print(len(l2))
# del l1
print(l1 + l2)
print(l1 * 5)
