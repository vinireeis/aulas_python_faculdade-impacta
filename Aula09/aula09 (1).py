# herança onde a classe carro e moto herdou tudo o que
#  tem na classe veículo a não ser que seja privado
class Veiculo:
    def __init__(self, marca, modelo, placa):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa

    def exibir_dados(self):
        print("Marca {}".format(self.marca))
        print("Modelo {}".format(self.modelo))
        print("Placa {}".format(self.placa))


class Carro(Veiculo):
    def __init__(self, marca, modelo, placa, portas):
        super().__init__(marca, modelo, placa)
        self.portas = portas

    def exibir_dados(self):
        super().exibir_dados()
        print("Portas {}".format(self.portas))


class Moto(Veiculo):
    def __init__(self, marca, modelo, placa, cilindrada):
        super().__init__(marca, modelo, placa)
        self.cilindrada = cilindrada

    def exibir_dados(self):
        super().exibir_dados()
        print("Cilindrada {}".format(self.cilindrada))

    def andar(self):
        print("moto andando")


carro1 = Carro("honda", "fit", "AAA-1234", 4)
carro1.exibir_dados()

moto1 = Moto("Honda", "CG", "BBB-4321", 300)
moto1.exibir_dados()
