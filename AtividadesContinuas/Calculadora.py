class Calculadora:
    def __init__(self, primeiro_valor, segundo_valor):
        self.primeiro_valor = primeiro_valor
        self.segundo_valor = segundo_valor

    def soma(self):
        return self.primeiro_valor + self.segundo_valor

    def sub(self):
        return self.primeiro_valor - self.segundo_valor

    def mult(self):
        return self.primeiro_valor * self.segundo_valor

    def div(self):
        return self.primeiro_valor / self.segundo_valor


teste = Calculadora(2, 5)
print("-" * 60)
print(teste.soma())
print("-" * 60)
print(teste.sub())
print("-" * 60)
print(teste.mult())
print("-" * 60)
print(teste.div())
