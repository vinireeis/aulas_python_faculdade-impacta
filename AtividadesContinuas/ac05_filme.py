# ATIVIDADE CONTÍNUA 05

# NOMES DOS ALUNOS: (MÁXIMO 6):
# ALUNO 1: nome
# ALUNO 2: nome
# ALUNO 3: nome
# ALUNO 4: nome
# ALUNO 5: nome
# ALUNO 6: nome


import sqlalchemy

from sqlalchemy import Column, Integer, String, Float, desc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

# Criar Conexão com Banco SQLITE
engine = sqlalchemy.create_engine("sqlite:///server.db")
connection = engine.connect()
Base = declarative_base(engine)
session = Session()


class Filme(Base):

    # FAZER O MAPEAMENTO DA TABELA

    # Método construtor
    def __init__(self, titulo, ano, genero, duracao, pais, diretor, elenco, avaliacao, votos):
        self.titulo = titulo
        self.ano = ano
        self.genero = genero
        self.duracao = duracao
        self.pais = pais
        self.diretor = diretor
        self.elenco = elenco
        self.avaliacao = avaliacao
        self.votos = votos


# Classe para interação com o Banco de Dados
class BancoDeDados:
    def criar_tabela(self):
        # Cria a tabela FILME no banco de dados
        connection.execute("""CREATE TABLE IF NOT EXISTS FILME(
                              ID INTEGER PRIMARY KEY,
                              TITULO VARCHAR(255) NOT NULL,
                              ANO INT NOT NULL,
                              GENERO VARCHAR(255) NOT NULL,
                              DURACAO INT NOT NULL,
                              PAIS VARCHAR(255) NOT NULL,
                              DIRETOR VARCHAR(255) NOT NULL,
                              ELENCO VARCHAR(255) NOT NULL,
                              AVALIACAO FLOAT NOT NULL,
                              VOTOS INT NOT NULL)""")

    def incluir(self, filme):
        '''
        Recebe um objeto Filme e armazena esse
        objeto no banco de dados.
        '''
        pass

    def incluir_lista(self, filmes):
        '''
        Recebe uma lista de objetos Filme e armazena esses
        objetos no banco de dados
        '''
        pass

    def alterar_avaliacao(self, filme, avaliacao):
        '''
        Recebe um objeto filme e altera sua avaliação de
        acordo com o valor do parametro avaliacao
        '''
        pass

    def excluir(self, id):
        '''
        Recebe o id de um filme e exclui o filme correspondente
        do banco de dados
        '''
        pass

    def buscar_todos(self):
        '''
        Realiza busca no banco de dados e retorna uma
        lista de objetos Filme com todos os registros,
        ordenados de forma crescente pelo titulo.
        '''
        pass

    def buscar_por_id(self, id):
        '''
        Realiza busca no banco de dados e retorna um
        objeto Filme de acordo com o seu id
        '''
        pass

    def buscar_por_ano(self, ano):
        '''
        Realiza busca no banco de dados e retorna uma
        lista de objetos Filme de um ano específico,
        ordenado pelo ID de forma crescente
        '''
        pass

    def buscar_por_genero(self, genero):
        '''
        Realiza busca no banco de dados e retorna uma
        lista de objetos Filme de um gênero específico,
        ordenados pelo titulo de forma crescente
        '''
        pass

    def buscar_por_elenco(self, ator):
        '''
        Realiza busca no banco de dados e retorna uma
        lista de objetos Filme que tenha um determinado ator/atriz como parte
        do elenco, ordenados pelo ano de lançamento em ordem crescente
        '''
        pass

    def buscar_melhores_do_ano(self, ano):
        '''
        Realiza busca no banco de dados e retorna uma lista de
        objetos Filme de um ano específico, com avaliação
        maior ou igual a 90
        Deve retornar ordenado pela avaliação de forma decrescente.
        DICA - utilize a função:
            .order_by(desc(Filme.avaliacao))
        '''
        pass

    def exportar_filmes(self, nome_arquivo):
        '''
        Exporta os dados contidos na tabela de filmes para um arquivo de texto
        O arquivo deve conter uma listagem dos filmes, ordenados pelos titulos
        dos filmes, contendo os dados de cada filme em uma linha, no formato:
        titulo;ano;genero;duracao;país;diretor;elenco;avaliacao;votos
        '''
        pass

    def importar_filmes(self, nome_arquivo):
        '''
        Recebe como parâmetro o nome de um arquivo de texto e importa os
        dados contidos no arquivo para o banco de dados.
        Considere que o arquivo contém uma listagem de filmes no formato:
        titulo;ano;genero;duracao;país;diretor;elenco;avaliacao;votos
        '''
        pass


# EXEMPLO DE PROGRAMA PRINCIPAL
banco = BancoDeDados()
banco.criar_tabela()
banco.importar_filmes('movies.txt')

# Busca todos os filmes
lista = banco.buscar_todos()
print('-'*60)
for f in lista:         # exibe lista de filmes
    print(f.id, f.titulo, f.ano, f.genero, f.duracao, f.pais, f.diretor, f.elenco, f.avaliacao, f.votos)

# Busca por ano
lista = banco.buscar_por_ano(2019)
print('-'*60)
for f in lista:         # exibe lista de filmes
    print(f.id, f.titulo, f.ano, f.genero, f.duracao, f.pais, f.diretor, f.elenco, f.avaliacao, f.votos)

# Busca por genero
lista = banco.buscar_por_genero('Crime')
print('-'*60)
for f in lista:         # exibe lista de filmes
    print(f.id, f.titulo, f.ano, f.genero)

# Busca por elenco
lista = banco.buscar_por_elenco('Nicole')
print('-'*60)
for f in lista:         # exibe lista de filmes
    print(f.id, f.titulo, f.ano, f.genero, f.duracao, f.pais, f.diretor, f.elenco, f.avaliacao, f.votos)

# Busca melhores do ano
lista = banco.buscar_melhores_do_ano('2019')
print('-'*60)
for f in lista:         # exibe lista de filmes
    print(f.id, f.titulo, f.ano, f.genero, f.duracao, f.pais, f.diretor, f.elenco, f.avaliacao, f.votos)


banco.exportar_filmes('saida.txt')
