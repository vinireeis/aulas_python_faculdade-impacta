import sqlalchemy

from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

#  Criar conexão com banco SQLITE

engine = sqlalchemy.create_engine("sqlite:///server.db")
connection = engine.connect()

#  Criar sessão com o Banco de Dados
Base = declarative_base(engine)
session = Session()


class Funcionario(Base):
    __tablename__ = 'FUNCIONARIO'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    nome = Column('NOME', String(255), nullable=False)
    idade = Column('IDADE', Integer, nullable=False)
    salario = Column('SALARIO', Float, nullable=False)

    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario


# Cria um arquivo de textopygame.examples.mask.main()
arquivo = open('saida.txt', 'w', encoding='UTF-8')

# Realiza consulta no banco de dados
resultado = session.query(Funcionario).order_by(Funcionario.nome).all()  # all opicional
for r in resultado:
    arquivo.write(r.nome.upper() + ';' + str(r.idade) + '-' + str(r.salario) + '\n')

#  Fechando arquivo e conexão com bancopygame.examples.mask.main()
arquivo.close()
connection.close()
