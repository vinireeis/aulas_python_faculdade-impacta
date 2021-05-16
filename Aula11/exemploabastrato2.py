from abc import ABC, abstractmethod


# interface = classe abstrata que possui apenas métodos abstratos
class Conta(ABC):
    def __init__(self, numero, titular):
        self.numero = numero
        self.titular = titular
        self.saldo = 0

    @abstractmethod
    def depositar(self, valor):
        pass

    @abstractmethod
    def sacar(self, valor):
        pass

    @abstractmethod
    def consultar_saldo(self):
        pass


class ContaEspecial(Conta):
    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor

    def consultar_saldo(self):
        print(self.saldo)


class ContaDigital(ContaEspecial):  # herdando de classe não abstrata
    pass  # Por herdar de uma classe não abstrata não é obrigatório os métodos


contadigital = ContaDigital(1234, "Reis")
contadigital.depositar(250)
contadigital.consultar_saldo()
