class AnimalTerrestre:
    def __init__(self, nome, altura):
        self.nome = nome
        self.altura = altura

    def andar(self):
        print("O animal terrestre andou")

    def comer(self):
        print("O animal terrestre comeu")


class AnimalAquatico:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie

    def nadar(self):
        print("O animal aquatico nadou")

    def comer(self):
        print("O animal aquatico comeu")


class Anfibio(AnimalAquatico, AnimalTerrestre):
    def __init__(self, nome, peso, altura):
        super().__init__(nome)
    '''AnimalTerrestre.__init__(self, nome, altura)    # chamada explicita, para dar preferencia a classe terrestre e não aquático mesmo estando em primeiro na herança'''
    '''AnimalAquatico.__init__(self, nome, especie)    # chamada explicita isso foi feito para puxar atributos das duas superclasses'''
        self.peso = peso


anfibio1 = Anfibio("sapo", "100g", "10cm", "anfibio")
anfibio1.andar()
anfibio1.comer()  # pegou da classe AnimalTerrestre pois é a primeira( tem preferencia)
anfibio1.nadar()
