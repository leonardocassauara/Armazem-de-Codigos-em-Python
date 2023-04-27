class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mover_para(self, x, y):
        print(f'O ponto de coordenadas ({self.x}, {self.y}) foi movido para as coordenadas ',end='')
        self.x = x
        self.y = y
        print(f'({self.x}, {self.y})')

    def distancia_para(self, point):
        eixo_x = self.x - point.x
        eixo_y = self.y - point.y
        if eixo_x < 0:
            eixo_x = eixo_x * -1
        if eixo_y < 0:
            eixo_y = eixo_y * -1
        dist = (eixo_x ** 2 + eixo_y ** 2) ** 0.5
        print(f'A distância entre os pontos ({self.x}, {self.y}) e ({point.x}, {point.y}) é de {dist:.1f} unidades')


# Output:
Ponto_1 = Ponto(5, 5)
Ponto_2 = Ponto(2,1)
print('—'*30)
Ponto_1.distancia_para(Ponto_2)
print('—'*30)
Ponto_1.mover_para(0, 0)
Ponto_1.distancia_para(Ponto_2)