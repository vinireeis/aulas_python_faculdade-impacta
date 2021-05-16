from abc import ABC, abstractmethod


class Funcionario(ABC):
    def __init__(self, nome, matricula, salario_base):
        self.nome = nome
        self.matricula = matricula
        self.salario_base = salario_base

    @abstractmethod
    def calcular_salario(self):
        pass


class Gerente(Funcionario):
    def calcular_salario(self):
        return self.salario_base * 2


class Vendedor(Funcionario):
    def calcular_salario(self):
        return self.salario_base * 1.10


class Assistente(Funcionario):
    def calcular_salario(self):
        return self.salario_base


g = Gerente("Vinicius", 9876, 2000)
v = Vendedor("João", 1234, 2000)
a = Assistente("Vitor", 3456, 2000)

lista = [g, v, a]

for x in lista:
    print(x.calcular_salario())
