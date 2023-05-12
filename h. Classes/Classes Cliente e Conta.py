# Classe "cliente" que os atributos são "nome, cpf, idade", classe "conta" que tenha os atributos "cliente, saldo,
# limite" e os métodos "sacar, depositar, consultar saldo" O programa deve conseguir criar clientes e contas.

class Cliente:
    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade


class Conta(Cliente):
    def __init__(self, nome, cpf, idade, saldo, limite):
        super().__init__(nome, cpf, idade)
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.saldo = saldo
        self.limite = limite

    def consultar_perfil(self):
        print('━' * 30)
        print(f'Bem vindo(a) {self.nome}!')
        print(f'CPF = {self.cpf}')
        print(f'Idade = {self.idade}')
        print(f'O seu saldo  é de R${self.saldo}')
        print(f'O seu limite é de R${self.limite}')
        print('━' * 30)

    def depositar(self, quantia):
        self.saldo += quantia
        print(f'Foram adicionados R${quantia} aos seus fundos. Totalizando R${self.saldo}')
        print('━' * 30)

    def sacar(self, quantia):
        if self.saldo >= quantia:
            self.saldo -= quantia
            print(f'Foram retirados R${quantia} dos seus fundos. Totalizando R${self.saldo}')
            print('━' * 30)
        else:
            print('Não há fundos suficientes para essa operação!')
            print('━' * 30)


# Output:
a = Conta('Alexandra', '032.123.456-30', 32, 1340, 4000)
a.consultar_perfil()
a.depositar(500)
a.sacar(2000)
a.sacar(1000)
