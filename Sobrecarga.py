"""
Exercicio seção 17 - parte 3
"""


class Pessoa:
    def __init__(self: object, codigo: str, nome: str, idade: str):
        self.__codigo = codigo
        self.__nome = nome
        self.__idade = idade

    def exibe(self, num=None):
        if num == 1:
            return f'Código: {self.__codigo}, Nome: {self.__nome}, Idade: {self.__idade}'
        return f'Código: {self.__codigo}, Nome: {self.__nome} \n'


class TestaPessoa(Pessoa):
    p1: Pessoa = Pessoa('456', 'Felipe', '28')
    print(p1.exibe())
    print(p1.exibe(1), '\n')
    print(p1.exibe([1]))

    def __init__(self: object, codigo: str, nome: str, idade=None):
        super().__init__(codigo, nome, idade)
        self.__codigo = codigo
        self.__nome = nome
        self.__idade = idade

    @classmethod
    def instanciar(cls):
        tp2 = cls('654', 'German', '32')
        return tp2

    def exibe(self, num=None):
        if num != 1:
            return f'Código: {self.__codigo} \nNome: {self.__nome} \n'
        return f'Código: {self.__codigo} \nNome: {self.__nome} \nIdade: {self.__idade}'


print(TestaPessoa.instanciar().exibe())

tp2 = TestaPessoa('987', 'Marcos', '36')
print(tp2.exibe(), '\n')
