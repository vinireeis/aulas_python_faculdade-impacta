import sqlalchemy

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

engine = sqlalchemy.create_engine("sqlite:///server.db")
connection = engine.connect()

Base = declarative_base(engine)
session = Session()


connection.execute("""CREATE TABLE IF NOT EXISTS PACIENTE(
                        ID INTEGER PRIMARY KEY,
                        NOME VARCHAR (50),
                        CPF CHAR (11),
                        IDADE INTEGER)
                   """)


class Paciente(Base):
    __tablename__ = "PACIENTE"
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    nome = Column('NOME', String(50), nullable=True)
    cpf = Column('CPF', String(11), nullable=True)
    idade = Column('IDADE', Integer, nullable=True)

    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade


connection.execute("""CREATE TABLE IF NOT EXISTS MEDICO(
                          ID INTEGER PRIMARY KEY,
                          NOME VARCHAR (50),
                          CRM VARCHAR (7),
                          ESPECIALIZACAO VARCHAR(300))
                   """)


class Medico(Base):
    __tablename__ = "MEDICO"
    id = Column("ID", Integer, primary_key=True, autoincrement=True)
    nome = Column('NOME', String(50), nullable=True)
    crm = Column('CRM', String(7), nullable=True)
    especializacao = Column('ESPECIALIZACAO', String(300), nullable=True)

    def __init__(self, nome, crm, especializacao):
        self.nome = nome
        self.crm = crm
        self.especializacao = especializacao


connection.execute("""CREATE TABLE IF NOT EXISTS EXAME(
                          ID INTEGER PRIMARY KEY,
                          ID_MEDICO INTEGER,
                          ID_PACIENTE INTEGER,
                          DESCRICAO VARCHAR (300),
                          RESULTADO VARCHAR (300))
                          """)


class Exame(Base):
    __tablename__ = "EXAME"
    id = Column("ID", Integer, primary_key=True, autoincrement=True)
    id_medico = Column("ID_MEDICO", Integer, nullable=True)
    id_paciente = Column("ID_PACIENTE", Integer, nullable=True)
    descricao = Column("DESCRICAO", String(300), nullable=True)
    resultado = Column("RESULTADO", String(300), nullable=True)

    def __init__(self, id_medico, id_paciente, descricao, resultado):
        self.id_medico = id_medico
        self.id_paciente = id_paciente
        self.descricao = descricao
        self.resultado = resultado


medico1 = Medico("Larissa", "948376", "PEDIATRIA")
paciente1 = Paciente("Vinicius", "41588156818", 27)
paciente2 = Paciente("Cintia", "25046008873", 47)

# inserindo médico e paciente no banco de dados
session.add(medico1)
session.add(paciente1)
session.add(paciente2)
session.commit()
# lista = [medico1, paciente1, paciente2]
# session.add_all(lista) para fazer todos de uma vez

exame1 = Exame(medico1.id, paciente1.id, "Exame de Tipagem Sanguinea", "AB+")
exame2 = Exame(medico1.id, paciente2.id, "Exame de Sorologia Covid", "Negativo")
session.add(exame1)
session.add(exame2)
session.commit()

# fazendo consulta no banco.

lista_medicos = session.query(Medico).order_by(Medico.nome).all()    # .all é opicional
lista_pacientes = session.query(Paciente).order_by(Paciente.nome).all()
lista_exames = session.query(Exame).all()

print('-' * 30)
for r in lista_medicos:
    print(r.id, r.nome, r.crm, r.especializacao)

print('-' * 30)
for s in lista_pacientes:
    print(s.id, s.nome, s.idade)

print('-' * 30)
for t in lista_exames:
    print(t.id, t.id_medico, t.id_paciente, t.descricao, t.resultado)

connection.close()
