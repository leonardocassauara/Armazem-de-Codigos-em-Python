class Animal:
    def __init__(self, nome, peso, idade):
        self.nome = nome
        self.peso = peso
        self.idade = idade

    def emitir_som(self):
        print('Argh!')


class Cachorro(Animal):
    def __init__(self, nome, peso, idade):
        super().__init__(nome, peso, idade)

    def cumprimentar(self):
        print(f'"Au au!" - {self.nome}\nPeso = {self.peso} kg Idade = {self.idade} anos')


# Output:
Meu_dog = Cachorro('Max', 25, 1)
Cachorro.cumprimentar(Meu_dog)
print('—' * 30)
