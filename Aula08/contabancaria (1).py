# Classe contabancaria
class ContaBancaria:
    def __init__(self, numero, titular, senha):
        self.numero = numero
        self.titular = titular
        self.__senha = senha
        self.__saldo = 0

    def __validar_senha(self, senha):   # método privado
        if senha == self.__senha:
            return True
        else:
            print("Senha invalida")
            return False

    def depositar(self, valor, senha):
        if self.__validar_senha(senha) is True:
            self.__saldo += valor

    def sacar(self, valor, senha):
        if self.__validar_senha(senha) is True:
            self.__saldo -= valor
        else:
            print("Senha invalida")

    def consultar(self):
        return self.__saldo


conta1 = ContaBancaria(1234, "Vinicius Reis", 4321)
valor = float(input("Valor para deposito:"))
senha = int(input("Informe sua senha: "))
conta1.depositar(valor, senha)
print("Seu saldo é: ", conta1.consultar())

valor = float(input("Qual valor deseja sacar:"))
senha = int(input("Informe sua senha: "))
conta1.sacar(valor, senha)
print("Seu saldo após o saque é: ", conta1.consultar())
