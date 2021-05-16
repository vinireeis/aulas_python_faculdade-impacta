from abc import ABC, abstractmethod


class Conta(ABC):   # Classe Abastrata
    def __init__(self, numero, titular):
        self.numero = numero
        self.titular = titular
        self.saldo = 0

    def consultar_saldo(self):
        print("Saldo: {}".format(self.saldo))

    @abstractmethod  # Metodo Abstrato
    def depositar(self, valor):
        pass

    @abstractmethod  # Metodo Abstrato
    def sacar(self, valor):
        pass


class ContaEspecial(Conta):
    def __init__(self, numero, titular, limite):
        super().__init__(numero, titular)
        self.limite = limite

    def sacar(self, valor):
        if valor <= self.saldo + self.limite:
            self.saldo -= valor  # polimorfismo de inclusão
        else:
            print("Saldo + limite insuficiente!")

    def depositar(self, valor):
        self.saldo += valor


class Poupanca(Conta):
    def sacar(self, valor):
        self.saldo -= valor

    def depositar(self, valor):
        self.saldo += valor


conta_especial = ContaEspecial(9437, "Vinicius Reis", 500)
conta_especial.depositar(300)
conta_especial.sacar(500)
conta_especial.consultar_saldo()
print('-' * 20)

poupanca = Poupanca(3214, "Oliveira")
poupanca.depositar(500)
poupanca.consultar_saldo()
