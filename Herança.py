"""
Exercicio seção 17 - parte 2
"""


class Equipamento:
    def __init__(self: object, energia: str, fonte: str):
        self.__energia: str = energia
        self.__fonte: str = fonte

    @property
    def energia(self):
        return self.__energia

    @property
    def fonte(self):
        return self.__fonte

    @energia.setter
    def energia(self, energia: str) -> None:
        self.__energia = energia

    @fonte.setter
    def fonte(self, fonte: str) -> None:
        self.__fonte = fonte

    def exibe(self):
        print(f'Energia: {self.__energia}, Fonte: {self.__fonte}')


class Computador(Equipamento):
    def __init__(self: object, mouse: str, teclado: str, energia: str, fonte: str):
        super().__init__(energia, fonte)
        self.__mouse: str = mouse
        self.__teclado: str = teclado

    @property
    def mouse(self):
        return self.__mouse

    @property
    def teclado(self):
        return self.__teclado

    @mouse.setter
    def mouse(self, mouse: str) -> None:
        self.__mouse = mouse

    @teclado.setter
    def teclado(self, teclado: str) -> None:
        self.__teclado = teclado

    def exibe(self):
        super(Computador, self).exibe()
        print(f'Mouse: {self.__mouse}, Teclado: {self.__teclado}')


class TestaEquipamento:
    def __init__(self):
        self.__equip: Equipamento = Equipamento('Ligada', 'Bivolt')
        self.__comp: Equipamento = Computador('Multilaser', 'Razer', 'Ligada', 'Bivolt')
        print(self.__dict__)

    def main(self):
        print('Equipamento:')
        self.__equip.exibe()
        print('\nComputador:')
        self.__comp.exibe()


teste = TestaEquipamento()
teste.main()
