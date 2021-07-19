from abc import ABC


class Conta(ABC):
    def __init__(self, n_conta, nome, saldo):
        self.n_conta = n_conta
        self.nome = nome
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print('-' * 20)
        print("Você depositou o valor de: {}.".format(valor))

    def extrato(self):
        print("Seu saldo é de {}.".format(self.saldo))

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print("Seu saque foi de {}.".format(valor))
        else:
            print(f"O valor de {valor} é maior que o saldo atual")
        print('-' * 20)


class ContaCorrente(Conta):
    pass


class ContaPoupanca(Conta):
    pass


class ContaEspecial(Conta):
    def __init__(self, n_conta, nome, saldo, limite):
        super().__init__(n_conta, nome, saldo)
        self.limite = limite

    def sacar(self, valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            print("Seu saque foi de {}.".format(valor))
        else:
            print(f"O valor {valor} é maior do que o saldo+limite disponível")
        print('-' * 20)


cc = ContaCorrente(1993, "Vinicius", 200)
print(cc.nome)
cc.extrato()
cc.depositar(1000)
cc.extrato()
cc.depositar(500)
cc.extrato()
cc.sacar(800)
cc.extrato()
print('-' * 20)
print('-' * 20)
print('-' * 20)


ce = ContaEspecial(118, "Larissa", 200, 100)
print(ce.nome)
ce.extrato()
ce.depositar(500)
ce.extrato()
ce.sacar(400)
ce.extrato()
ce.sacar(550)
