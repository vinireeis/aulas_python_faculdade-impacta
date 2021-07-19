class Pessoa:
    def __init__(self, nome, idade, cpf, rg):
        # atributos publicos
        self.nome = nome
        self.idade = idade
        # atributods privados
        self.__cpf = cpf
        self.__rg = rg

# métodos get: retornar o valor de um atributo privado
    def get_cpf(self):
        return self.__cpf

    def get_rg(self):
        return self.__rg

# métodos set: alterar o valor do atributo privado
    def set_cpf(self, cpf):
        self.__cpf = cpf

    def set_rg(self, rg):
        self.__rg = rg


pessoa1 = Pessoa('Vinicius', 25, "41588156818", "425731753")
pessoa1.idade = 27      # altera a idade
# pessoa1.__cpf = "22222222222" # altera o cpf pq esta dentro da classe
pessoa1.set_cpf("99999999911")  # altera o cpf metodo set
pessoa1.set_rg("888885553")  # altera o rg
print("Nome: ", pessoa1.nome)
print("CPF: ", pessoa1.get_cpf())   # forma de printar o atributo privado
print("RG :", pessoa1.get_rg())  # forma de printar o atributo privado
