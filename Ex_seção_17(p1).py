"""
Exercicios Seção 17 - Parte 1
"""


# 1.0
class Pessoa:
    def __init__(self: object, nome: str, endereco: str, telefone: str):
        self.nome: str = nome
        self.endereco: str = endereco
        self.telefone: str = telefone

    def imprimir(self):
        print(f'{self.nome}, {self.endereco}, {self.telefone}')


p1 = Pessoa('Marcelo', 'Rua General Severiano número 15', '7234-8965')
p1.imprimir()


# 3.0
class Quadrado:
    def __init__(self: object, lado: int, area: int, perimetro: int):
        self.lado: int = lado
        self.area: int = area
        self.perimetro: int = perimetro

    def calcular_area(self):
        return self.lado * self.lado

    def calcular_perimetro(self):
        return 4 * self.lado

    def imprimir(self):
        print(f'O quadrado tem lado {self.lado}, {self.area} de área e {self.perimetro} de perímetro')


q1 = Quadrado(4, 16, 16)
q1.calcular_area()
q1.calcular_perimetro()
q1.imprimir()

# 9.0


class Moto:
    def __init__(self: object, marca: str, modelo: str, cor: str, marcha: str):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.marcha = marcha

    def imprimir(self):
        print(f'A moto é uma {self.marca} {self.modelo} de cor {self.cor} e com marcha{self.marcha}')


m1 = Moto('Kawasaki', 'Ninja', 'Preta', ' 4')
m1.imprimir()
