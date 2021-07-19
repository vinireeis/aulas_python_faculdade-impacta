class Conta:
    def __init__(self, numero, titular):
        self.numero = numero
        self.titular = titular
        self.saldo = 0

    def consultar_saldo(self):
        print("Saldo: {}".format(self.saldo))

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo Insuficiente")


class ContaEspecial(Conta):
    def __init__(self, numero, titular, limite):
        super().__init__(numero, titular)
        self.limite = limite

    def sacar(self, valor):
        if valor <= self.saldo + self.limite:
            self.saldo -= valor  # polimorfismo de inclusão
        else:
            print("Saldo + limite insuficiente!")


conta = Conta(123, "Vinicius")
conta.depositar(200)
conta.sacar(300)

conta_especial = ContaEspecial(9437, "Vinicius Reis", 500)
conta_especial.depositar(300)
conta_especial.sacar(500)
print(conta_especial.saldo)
