class Veículo:
    def __init__(self, tipo, cor):
        self.tipo = tipo
        self.cor = cor

    def mover(self):
        print('Estou me movendo weee')


class Carro(Veículo):
    def __init__(self, tipo, cor):
        super().__init__(tipo, cor)
        self.tipo = tipo
        self.cor = cor

    def mover(self):
        print('O carro está se movendo')


class Avião(Veículo):
    def __init__(self, tipo, cor):
        super().__init__(tipo, cor)
        self.cor = cor
        self.tipo = tipo

    def mover(self):
        print('O avião está voando')


b = Carro('Uno', 'Rosa')
c = Avião('Boeing', 'Preto')
b.mover()
c.mover()