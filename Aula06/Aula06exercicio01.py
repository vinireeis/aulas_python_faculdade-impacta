class Livro:
    def __init__(self, titulo, autor, quantidade_paginas):
        self.titulo = titulo
        self.autor = autor
        self.quantidade_paginas = quantidade_paginas

    def exibir_dados(self):
        print("_______________________________________________")
        print("Título:", self.titulo)
        print("Autor:", self.autor)
        print("Número de páginas:", self.quantidade_paginas)


#  criar objetivos
Livro1 = Livro("Um estudo em vermelho", "Vinicius", 237)
Livro2 = Livro(" P.s. Eu te amo", "Larissa", 483)
#  exibir objetos
Livro1.exibir_dados()
Livro2.exibir_dados()
