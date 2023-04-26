class Retângulo:
    def __init__(self, largura=3, altura=2):
        self.largura = float(largura)
        self.altura = float(altura)

    def perimetro(self):
        per = (self.largura + self.altura) * 2
        return per

    def area(self):
        ar = self.largura * self.altura
        return ar


# Output:
elemento = Retângulo(4, 5)
print(f'O perímetro do retângulo {elemento.largura:.0f}x{elemento.altura:.0f} é de {elemento.perimetro()}')
print(f'A área      do retângulo {elemento.largura:.0f}x{elemento.altura:.0f} é de {elemento.area()}')