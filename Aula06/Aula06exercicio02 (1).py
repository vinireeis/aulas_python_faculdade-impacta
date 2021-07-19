'''
Classe Triangulo
Atributos:
-> lado_a
-> lado_b
-> lado_c

Métodos:
calcular_perimetro
Solicitar dados ao usuário para criar um objeto
'''


class Triangulo:
    def __init__(self, lado_a, lado_b, lado_c):
        self.lado_a = lado_a
        self.lado_b = lado_b
        self.lado_c = lado_c

    def calcular_perimetro(self):
        return self.lado_a + self.lado_b + self.lado_c


#  inputar dados
'''nome da variavel não precisa ser igual ao self.ladoa = lado_a'''

a = float(input("Informe o tamanho do primeiro lado:"))
b = float(input("Informe o tamanho do segundo lado:"))
c = float(input("Informe o tamanho do terceiro lado:"))

#  criar objeto
Triangulo1 = Triangulo(a, b, c)
