'''
Implemente as classes Episodio e Serie.

A classe Episodio possui o número do episódio, o número da temporada a
qual o episódio pertence, o nome do episódio e a sua duração em minutos.
O construtor da classe Episodio deve inicializar os seus atributos com os
valores recebidos por parâmetro.

A classe Serie possui o nome da serie e uma lista de episódios.
O construtor da classe Serie deve inicializar o nome da serie com o valor
recebido por parametro e a lista de episódios como vazia.
A classe Serie deve possuir o método incluir_episodio, que insere um
episódio na lista de episódios.
A classe Serie deve possuir o método buscar_episodios, que retorna a
lista com todos os episódios de uma determinada temporada da série.

'''


# ------------------- IMPLEMENTE AS CLASSES AQUI ------------------- #

class Episodio:
    def __init__(self, numero, temporada, nome, duracao):
        self.numero = numero
        self.temporada = temporada
        self.nome = nome
        self.duracao = duracao


class Serie:
    def __init__(self, nome):
        self.nome = nome
        self.lista_episodios = []

    def incluir_episodio(self, episodio):
        self.lista_episodios.append(episodio)
        print('Episodio adicionado com sucesso')
        print('-' * 60)

    def buscar_episodios(self, temporada):
        lista = []
        for r in self.lista_episodios:
            if r.temporada == temporada:
                lista.append(r)
        return lista


# ----------------------- PROGRAMA PRINCIPAL ----------------------- #
serie1 = Serie("Game of Thrones")

ep1 = Episodio(1, 1, "Winter Is Coming", 63)
ep2 = Episodio(2, 1, "The Kingsroad", 56)
ep3 = Episodio(3, 1, "Lord Snow", 103)
ep4 = Episodio(1, 8, "Winterfell", 54)
ep5 = Episodio(2, 8, "A Knight of the Seven Kingdoms", 58)
ep6 = Episodio(3, 8, "The Long Night", 82)

serie1.incluir_episodio(ep1)
serie1.incluir_episodio(ep2)
serie1.incluir_episodio(ep3)
serie1.incluir_episodio(ep4)
serie1.incluir_episodio(ep5)
serie1.incluir_episodio(ep6)

serie2 = Serie("Stranger Things")

ep1 = Episodio(1, 1, "Chapter One: The Vanishing of Will Byers", 47)
ep2 = Episodio(2, 1, "Chapter Two: The Weirdo on Maple Street", 55)
ep3 = Episodio(3, 1, "Chapter Three: Holly, Jolly", 51)
ep4 = Episodio(1, 2, "Chapter One: MADMAX", 48)
ep5 = Episodio(2, 2, "Chapter Two: Trick or Treat, Freak", 56)
ep6 = Episodio(3, 2, "Chapter Three: The Pollywog", 51)

serie2.incluir_episodio(ep1)
serie2.incluir_episodio(ep2)
serie2.incluir_episodio(ep3)
serie2.incluir_episodio(ep4)
serie2.incluir_episodio(ep5)
serie2.incluir_episodio(ep6)

# Exibe o nome de todos os episódios da 8ª temporada de Game of Thrones
lista = serie1.buscar_episodios(8)
for ep in lista:
    print(ep.nome)

# Exibe o nome de todos os episódios da 1ª temporada de Stranger Things
lista = serie2.buscar_episodios(1)
for ep in lista:
    print(ep.nome)
