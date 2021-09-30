import sqlalchemy

from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

# Criar Conexão com Banco SQLITE
# caso o arquivo de banco não exista, ele será criado
engine = sqlalchemy.create_engine("sqlite:///server.db")
connection = engine.connect()

# Criar sessão com o Banco de Dados
Base = declarative_base(engine)
session = Session()

connection.execute("""CREATE TABLE IF NOT EXISTS FUNCIONARIO(
                      ID INTEGER PRIMARY KEY,
                      NOME VARCHAR(255) NOT NULL,
                      IDADE INT NOT NULL,
                      SALARIO FLOAT NOT NULL)""")


class Funcionario(Base):
    __tablename__ = "FUNCIONARIO"
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    nome = Column('NOME', String(255), nullable=False)
    idade = Column('IDADE', Integer, nullable=False)
    salario = Column('SALARIO', Float, nullable=False)

    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario


func1 = Funcionario("Vinicius", 27, 2500)
func2 = Funcionario("Cintia", 47, 3250.50)
func3 = Funcionario("Larissa", 23, 1400.7)

lista = [func1, func2, func3]

session.add_all(lista)
session.commit()
print('-' * 50)
result = session.query(Funcionario)
for i in result:
    print(f'{i.nome}, {i.idade}, {i.salario:.2f}')
print('-' * 50)
print('-' * 50)
result = session.query(Funcionario).filter(Funcionario.salario > 1500)
for i in result:
    print(f'{i.nome}, {i.idade}, {i.salario:.2f}')
