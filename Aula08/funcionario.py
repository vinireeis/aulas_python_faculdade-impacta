class Funcionario:
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.__salario = salario    # atributo privado

    def set_salario(self, salario):
        if salario > 0:
            self.__salario = salario
        else:
            print("Valor invalido")

    def get_salario(self):
        return self.__salario


funcionario1 = Funcionario("Viniciuis", 27, 3500)
funcionario1.nome = "Vinicius Reis"
funcionario1.idade = 28
funcionario1.__salario = 3000  # erro sem metodo set
funcionario1.set_salario(5000)  # sem erro por usar metodo set para atributo privado
print("Nome: ", funcionario1.nome)
print("Salario: ", funcionario1.get_salario())
