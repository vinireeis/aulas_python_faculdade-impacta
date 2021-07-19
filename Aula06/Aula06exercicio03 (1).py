'''
Classe Televisao
Atributos:
-> canal = None
-> volume = 0

Metodos:
aumentar_volume: aumenta em 1 unidade
diminuir_volume: diminui em 1 unidade
alterar_canal(canal)
'''


class Televisao:
    def __init__(self):
        self.canal = None
        self.volume = 0

    def aumentar_volume(self):
        self.volume += 1

    def diminuir_volume(self):
        self.volume -= 1

    def alterar_canal(self, canal):
        self.canal = canal


#  criar objeto
tv = Televisao()
tv.aumentar_volume()
tv.aumentar_volume()
tv.aumentar_volume()
tv.diminuir_volume()
tv.alterar_canal(5)
tv.alterar_canal(11)

print("Volume é:", tv.volume)
print("canal é:", tv.canal)
