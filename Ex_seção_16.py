"""
Exercícios - Orientação a objetos
"""


# 1.0
class Pessoa:
    def __init__(self: object, nome: str, idade: int, altura: float):
        self.__nome: str = nome
        self.__idade: int = idade
        self.__altura: float = altura

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome: str) -> None:
        self.__nome = nome

    def get_idade(self):
        return self.__idade

    def set_idade(self, idade: str) -> None:
        self.__idade = idade

    def get_altura(self):
        return self.__altura

    def set_altura(self, altura: str) -> None:
        self.__altura = altura

    def dados(self):
        print(f'{self.__nome} tem {self.__idade} anos e {self.__altura}cm de altura')


dado = Pessoa('Jorge', 26, 1.81)
dado.dados()


# 2.0
class Agenda:
    __armazenamento = []

    def armazena_pessoa(self: object, pessoa):
        if len(self.__armazenamento) < 10:
            self.__armazenamento.append(pessoa)
        else:
            print('Limite alcançado!')

    def remove_pessoa(self: object, nome_remocao):
        for pessoa in self.__armazenamento:
            if pessoa.get_nome() == nome_remocao:
                self.__armazenamento.remove(pessoa)
                print('Pessoa removida!')
                return True
        print('Pessoa não encontrada.')
        return False

    def buscar_pessoa(self: object, name):
        for pessoa in self.__armazenamento:
            if pessoa.get_nome() == name:
                print(f'A pessoa está localizada no índice: {self.__armazenamento.index(pessoa)}')
                return True
            print('Pessoa não localizada.')
        return False

    def imprimir_agenda(self: object):
        for pessoa in self.__armazenamento:
            print(f'Nome:{Pessoa.get_nome(pessoa)}')
            print(f'Idade:{Pessoa.get_idade(pessoa)} ')
            print(f'Altura:{Pessoa.get_altura(pessoa)}\n ')

    def imprimir_dados(self: object, posicao):
        if 0 <= posicao <= len(self.__armazenamento):
            lista = self.__armazenamento
            pessoa = lista[posicao]
            print(f'Nome: {Pessoa.get_nome(pessoa)}')
            print(f'Idade: {Pessoa.get_idade(pessoa)}')
            print(f'Altura: {Pessoa.get_altura(pessoa)}')


p1 = Pessoa('Luis', 18, 1.65)
p2 = Pessoa('Larissa', 19, 1.70)
p3 = Pessoa('Rafaela', 22, 1.75)
p4 = Pessoa('Luisa', 18, 1.68)
p5 = Pessoa('Thayane', 18, 1.62)
p6 = Pessoa('Carlos', 22, 1.73)
p7 = Pessoa('Sarah', 20, 1.59)
p8 = Pessoa('Daniel', 19, 1.74)
p9 = Pessoa('João Pedro', 21, 1.76)
p10 = Pessoa('Gabriela', 19, 1.66)

colecao_pessoa = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]
agenda: Agenda = Agenda()
for pessoa in colecao_pessoa:
    Agenda.armazena_pessoa(agenda, pessoa)

nome: str = 'Luis'
Agenda.remove_pessoa(agenda, nome)
print(Agenda.imprimir_agenda(agenda))

nome: str = 'Carlos'
print(Agenda.buscar_pessoa(agenda, nome))
print(Agenda.imprimir_agenda(agenda))

Agenda.imprimir_dados(agenda, 0)
print(Agenda.imprimir_agenda(agenda))


# 3.0
class Elevador:
    def __init__(self: object, total_andares: int, capacidade: int):
        self.total_andares: int = total_andares
        self.capacidade: int = capacidade
        self.pessoas: int = 0
        self.andar_atual: int = 0

    def entra(self):
        if self.pessoas < self.capacidade:
            self.pessoas += 1
        else:
            print(f'O elevador está cheio!')

    def sai(self):
        if self.pessoas > 0:
            self.pessoas -= 1
        else:
            print(f'O elevador está vazio!')

    def sobe(self):
        if self.andar_atual < self.total_andares:
            self.andar_atual += 1
        else:
            print(f'Já estamos no último andar!')

    def desce(self):
        if self.andar_atual > 0:
            self.andar_atual -= 1
        else:
            print(f'Estamos no térreo!')

    def get_andar_atual(self):
        return self.andar_atual

    def get_total_andares(self):
        return self.total_andares

    def get_capacidade(self):
        return self.capacidade

    def get_pessoas_elevador(self):
        return self.pessoas

    def set_andar_atual(self, andar) -> None:
        self.andar_atual = andar

    def set_total_andares(self, total) -> None:
        self.total_andares = total

    def set_capacidade(self, capacidade) -> None:
        self.capacidade = capacidade

    def set_pessoas_elevador(self, pessoas) -> None:
        self.pessoas = pessoas


Elevador(10, 6)
print(Elevador)


# 4.0

class Televisao:
    def __init__(self: object, canal=0, volume=10):
        self.canal: int = canal
        self.volume: int = volume

    def controle_volume(self, valor):
        self.volume += valor

    def controle_canal(self, valor):
        if valor > 1:
            self.canal = valor
        else:
            self.canal += valor


class ControleRemoto:
    def __init__(self: object, televisao: Televisao):
        self.televisao = televisao

    def alterar_volume(self, valor):
        self.televisao.controle_volume(valor)
        print(f'O volume da TV agora é {self.televisao.volume}')

    def alterar_canal(self, valor):
        self.televisao.controle_canal(valor)
        print(f'O canal da TV agora é {self.televisao.canal}')


tv = Televisao()
cr = ControleRemoto(tv)

cr.alterar_volume(4)
cr.alterar_canal(8)
