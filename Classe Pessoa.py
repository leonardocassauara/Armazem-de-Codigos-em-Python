class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def aniversário(self):
        self.idade += 1

    def cumprimentar(self):
        print(f'Olá meu nome é {self.nome} e eu tenho {self.idade} anos!')

# Output:
abacate = Pessoa("Jonathan", 30)
abacate.cumprimentar()
print('—'*30)
abacate.aniversário()
abacate.cumprimentar()