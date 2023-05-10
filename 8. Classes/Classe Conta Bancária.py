class ContaBancaria:
    def __init__(self, saldo, titular):
        self.saldo = saldo
        self.titular = titular
        self.novo_saldo = self.saldo

    def depositar(self, quantia):
        self.novo_saldo = float(self.saldo) + float(quantia)
        print(f'{self.titular}! O valor de R$'f'{quantia:.2f}'.replace('.',','),'foi depositado ao seu saldo de R$'f'{self.saldo:.2f}'.replace('.',','),'\nO valor do seu novo saldo é R$'f'{self.novo_saldo:.2f}'.replace('.',','))

    def sacar(self, quantia):
        print(f'{self.titular}! O valor de R$'f'{quantia:.2f}'.replace('.', ','),
              'foi sacado do seu saldo de R$'f'{self.novo_saldo:.2f}'.replace('.', ','))
        self.novo_saldo = float(self.novo_saldo) - float(quantia)
        print('O valor do seu novo saldo é R$'f'{self.novo_saldo:.2f}'.replace('.', ','))



# Output:
conta = ContaBancaria(100, "Anastacia")
conta.depositar(200)
conta.sacar(50)