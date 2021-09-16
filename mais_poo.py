"""
Mais exercícios POO
"""


# 1.0
class Livro:
    def __init__(self: object, nome: str, paginas: int, autor: str, preco: int):
        self.nome: str = nome
        self.paginas: int = paginas
        self.autor: str = autor
        self.preco: int = preco

    def get_preco(self: object):
        print(f'O valor do livro é {self.preco}')

    def set_preco(self: object):
        print(f'O valor do livro agora é {self.preco} + {20.00}')

    def dados(self):
        print(f'Nome: {self.nome}, Páginas: {self.paginas}, Autor: {self.autor}, Preço: {self.preco}')


l1 = Livro('The Rational Male', 140, 'Rollo Tomassi', 60)
l1.get_preco()
l1.set_preco()
l1.dados()
