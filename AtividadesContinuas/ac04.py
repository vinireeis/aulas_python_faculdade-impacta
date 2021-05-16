# PROGRAMAÇÃO ORIENTADA A OBJETOS
# ATIVIDADE CONTÍNUA 04

# INSIRA ABAIXO O NOME DOS ALUNOS DO GRUPO
# ALUNO 1: Vinicius Dos Reis Oliveira

class Pessoa:
    def __init__(self, nome, dt_nasc, rg, tel):
        self.nome = nome
        self.dt_nasc = dt_nasc
        self.rg = rg
        self.tel = tel


class Instrutor(Pessoa):
    def __init__(self, nome, dt_nasc, rg, tel):
        super().__init__(nome, dt_nasc, rg, tel)
        self.titulacao = None
        self.turmas = []

    def incluir_turma(self, turma):
        self.turmas.append(turma)

    def set_titulacao(self, titulacao):
        self.titulacao = titulacao


class Aluno(Pessoa):
    def __init__(self, nome, dt_nasc, rg, tel, codigo, dt_matricula):
        super().__init__(nome, dt_nasc, rg, tel)
        self.codigo = codigo
        self.dt_matricula = dt_matricula
        self.endereco = None
        self.altura = None
        self.peso = None
        self.turmas = []
        self.__faltas = 0

    def incluir_faltas(self, quantidade):
        self.__faltas += quantidade

    def get_faltas(self):
        return self.__faltas

    def incluir_turma(self, turma):
        self.turmas.append(turma)

    def set_endereco(self, endereco):
        self.endereco = endereco

    def set_altura(self, altura):
        self.altura = altura

    def set_peso(self, peso):
        self.peso = peso


class Academia:
    def __init__(self, nome):
        self.nome = nome
        self.turmas = []

    def incluir_turmas(self, turma):
        self.turmas.append(turma)


class Turma:
    def __init__(self, nome, atividade):
        self.nome = nome
        self.atividade = atividade
        self.dt_inicial = None
        self.dt_final = None
        self.tempo_aula = None
        self.horario_aula = None
        self.alunos = []
        self.monitor = None
        self.instrutor = None

    def set_dt_inicial(self, dt_inicial):
        self.dt_inicial = dt_inicial

    def set_dt_final(self, dt_final):
        self.dt_final = dt_final

    def set_tempo_aula(self, tempo_aula):
        self.tempo_aula = tempo_aula

    def set_horario_aula(self, horario_aula):
        self.horario_aula = horario_aula

    def get_lista_alunos(self):
        print(self.alunos)

    def incluir_aluno(self, aluno):
        self.alunos.append(aluno)

    def set_monitor(self, monitor):
        self.monitor = monitor

    def set_instrutor(self, instrutor):
        self.instrutor = instrutor


#  criando a academia, turmas, alunos, monitor, instrutor
cobrakai = Academia("Academia Cobra Kai")
print(cobrakai.nome)
judo = Turma("Turma A", "Judo")
karate = Turma("Turma B", "Karatê")
cobrakai.incluir_turmas(judo.nome)
cobrakai.incluir_turmas(karate.nome)
print(cobrakai.turmas[0])
print(cobrakai.turmas[1])
print("-" * 100)
print(f"Existem as atividades de {judo.atividade} e {karate.atividade}.")
print("-" * 100)
aluno1 = Aluno("Vinicius Reis", "09-11-1993", "42.573.175-1",
               "11952945737", 123, "05-05-2021")
aluno2 = Aluno("Larissa Costa", "22-01-1997", "250.260.088-75",
               "1126467579", 456, "06-05-2021")
aluno3 = Aluno("Cintia Oliveira", "23-06-1990", "250.360.078-54",
               "11956707862", 789, "04-05-2021")
print(f"Temos os alunos {aluno1.nome}, {aluno2.nome} e {aluno3.nome}")
print("-" * 100)
judo.set_monitor(aluno1)
karate.set_monitor(aluno2)
print(f"O monitor da turma de {judo.nome} é o aluno {judo.monitor.nome}e",
      f"o monitor da {karate.nome} é a {karate.monitor.nome}.")
instrutor1 = Instrutor("Paulo", "13-01-1985", "250.088.175.74", "11945945637")
instrutor2 = Instrutor("Debora", "13-04-1980", "333.444.555.66", "11998855443")
judo.set_instrutor(instrutor1)
karate.set_instrutor(instrutor2)
print("-" * 100)
print(f"Temos dois instrutores, {instrutor1.nome} e {instrutor2.nome}.")
print("-" * 100)
karate.incluir_aluno(aluno1)
judo.incluir_aluno(aluno2)
judo.incluir_aluno(aluno3)
print("Os alunos de Judo são {}, {} e Karate o {}".format(judo.alunos[0].nome,
      judo.alunos[1].nome, karate.alunos[0].nome))
print("-" * 100)
judo.alunos[0].incluir_faltas(10)
karate.alunos[0].incluir_faltas(2)
print(f"O aluno {aluno1.nome}, tem {karate.alunos[0].get_faltas()} faltas.")
print("-" * 100)
