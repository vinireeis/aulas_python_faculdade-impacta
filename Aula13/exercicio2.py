import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

# Criar Conexão com Banco SQLITE
# caso o arquivo de banco não exista, ele será criado
engine = sqlalchemy.create_engine("sqlite:///server.db")
connection = engine.connect()

# Criar sessão com o Banco de Dados
Base = declarative_base(engine)
session = Session()

connection.execute("""CREATE TABLE IF NOT EXISTS AUTOR(
           ID INTEGER PRIMARY KEY,
           NOME varchar(255) NOT NULL)""")

connection.execute("""CREATE TABLE IF NOT EXISTS LIVRO(
           ID INTEGER PRIMARY KEY,
           TITULO VARCHAR(255) NOT NULL,
           PAGINAS INT NOT NULL,
           AUTOR_ID INT NOT NULL)""")
