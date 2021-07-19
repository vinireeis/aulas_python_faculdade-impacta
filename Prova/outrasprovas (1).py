# Prova 2
class Funcionario:
    def __init__(self, nome, idade, sexo, matricula, salario):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.matricula = matricula
        self.salario = salario

    def valor_inss(self):
        x = self.salario * 0.12
        return x


class Gerente(Funcionario):
    def __init__(self, nome, idade, sexo, matricula, salario, setor):
        super().__init__(nome, idade, sexo, matricula, salario)
        self.setor = setor


class Vendedor(Funcionario):
    def __init__(self, nome, idade, sexo, matricula, salario, valor_vendas):
        super().__init__(nome, idade, sexo, matricula, salario)
        self.valor_vendas = valor_vendas

    def valor_inss(self):
        x = self.salario * 0.12 + self.valor_vendas * 0.10
        return x


# -------------- PROGRAMA PRINCIPAL (não deve ser alterado) -----------------
diretor = Funcionario("Carla", 40, "feminino", 224321, 7000.00)
gerente1 = Gerente("João", 35, "masculino", 123456, 4000.00, "vendas")
gerente2 = Gerente("Maria", 30, "feminino", 345672, 3500.00, "financeiro")
vendedor1 = Vendedor("Pedro", 22, "masculino", 222332, 1500.00, 3500.00)
vendedor2 = Vendedor("Fernanda", 25, "feminino", 878332, 2000.00, 5000.00)

print(diretor.valor_inss())                         # 840.0
print(gerente1.valor_inss())                        # 480.0
print(gerente2.valor_inss())                        # 420.0
print(vendedor1.valor_inss())                       # 530.0
print(vendedor2.valor_inss())                       # 740.0
# ---------------------------------------------------------------------------


# Prova 3
class Empresa:
    def __init__(self):
        self.funcionarios = []

    def incluir_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def quantidade_funcionarios(self):
        tot = 0
        for r in self.funcionarios:
            if r.get_salario() > 2000:
                tot += 1
        return tot


class Funcionario:
    def __init__(self, nome, salario):
        self.__nome = nome
        self.__salario = salario

    def get_nome(self):
        return self.__nome

    def get_salario(self):
        return self.__salario


func1 = Funcionario('John', 4000)
print("Nome:", func1.get_nome())                            # Nome: John
print("Salário:", func1.get_salario())                      # Salário: 4000

func2 = Funcionario('George', 2500)
print("Nome:", func2.get_nome())                            # Nome: George
print("Salário:", func2.get_salario())                      # Salário: 2500

func3 = Funcionario('Mathew', 1800)
print("Nome:", func3.get_nome())                            # Nome: Mathew
print("Salário:", func3.get_salario())                      # Salário: 1800

empresa = Empresa()
empresa.incluir_funcionario(func1)
empresa.incluir_funcionario(func2)
empresa.incluir_funcionario(func3)
print("Quantidade:", empresa.quantidade_funcionarios())     # Quantidade: 2
# ---------------------------------------------------------------------------


# Prova 4
class Pessoa:
    def __init__(self, nome):
        self.nome = nome


class Aluno(Pessoa):
    def __init__(self, nome, ra):
        super().__init__(nome)
        self.ra = ra
        self.notas = []

    def cadastrar(self, nota):
        self.notas.append(nota)

    def calcular_media(self):
        lista = []
        x = min(self.notas)
        for r in self.notas:
            if r != x:
                lista.append(r)
        x = sum(lista)/4
        return x


# -------------- PROGRAMA PRINCIPAL (não deve ser alterado) -----------------
aluno1 = Aluno(123456, 'João')
aluno1.cadastrar(8.0)
aluno1.cadastrar(7.0)
aluno1.cadastrar(9.0)
aluno1.cadastrar(6.0)
aluno1.cadastrar(7.0)
print("Média:", aluno1.calcular_media())       # Média: 7.75

aluno2 = Aluno(123456, 'Maria')
aluno2.cadastrar(10.0)
aluno2.cadastrar(9.0)
aluno2.cadastrar(6.5)
aluno2.cadastrar(5.0)
aluno2.cadastrar(7.5)
print("Média:", aluno2.calcular_media())       # Média: 8.25'''


# ---------------------------------------------------------------------------
'''Considere o sistema de uma loja virtual e implemente as classes Produto,
Item e ItemDesconto.

A classe Produto possui os atributos codigo, descricao e preco.
A classe Item possui os atributos produto e quantidade.
A classe ItemDesconto deve herdar da classe Item.

A classe Item deve implementar o método calcular_preco, que retorna como valor
o resultado da multiplicação do preço do produto pela quantidade de itens.
A classe ItemDesconto deve sobrescrever o método calcular_preco e aplicar um
desconto de 20% no preço total calculado.'''


# Prova 5
# --------------------- IMPLEMENTE SEU CÓDIGO AQUI --------------------------
class Produto:
    def __init__(self, codigo, descricao, preco):
        self.codigo = codigo
        self.descricao = descricao
        self.preco = preco


class Item:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade

    def calcular_preco(self):
        return self.produto.preco * self.quantidade


class ItemDesconto(Item):
    def calcular_preco(self):
        return (self.produto.preco * self.quantidade) - (self.produto.preco * self.quantidade) * 0.20


# -------------- PROGRAMA PRINCIPAL (não deve ser alterado) -----------------
produto1 = Produto(1, "Produto 1", 30.0)
produto2 = Produto(2, "Produto 2", 50.0)

item1 = Item(produto1, 5)
item2 = ItemDesconto(produto1, 5)
item3 = ItemDesconto(produto2, 10)

print("Total:", item1.calcular_preco())       # Total: 150.0
print("Total:", item2.calcular_preco())       # Total: 120.0
print("Total:", item3.calcular_preco())       # Total: 400.0
