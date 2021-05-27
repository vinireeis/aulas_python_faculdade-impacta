# ATIVIDADE CONTÍNUA 05

# NOMES DOS ALUNOS: (MÁXIMO 6):
# ALUNO 1: Vinicius Dos Reis Oliveira RA 1701731
# ALUNO 2: Karina Watanabe

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
    __tablename__ = "FILME"
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    titulo = Column('TITULO', String(255), nullable=True)
    ano = Column('ANO', Integer, nullable=True)
    genero = Column('GENERO', String(255), nullable=True)
    duracao = Column('DURACAO', Integer, nullable=True)
    pais = Column('PAIS', String(255), nullable=True)
    diretor = Column('DIRETOR', String(255), nullable=True)
    elenco = Column('ELENCO', String(255), nullable=True)
    avaliacao = Column('AVALIACAO', Float, nullable=True)
    votos = Column('VOTOS', Integer, nullable=True)

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
        self.filme = filme
        session.add(filme)
        session.commit()

    def incluir_lista(self, filmes):
        '''
        Recebe uma lista de objetos Filme e armazena esses
        objetos no banco de dados
        '''
        self.filmes = filmes
        session.add_all(filmes)
        session.commit()

    def alterar_avaliacao(self, filme, avaliacao):
        '''resultado = session.query(Filme).filter(Filme.titulo == filme)
            return resultado.avaliacao = avaliacao
        Recebe um objeto filme e altera sua avaliação de
        acordo com o valor do parametro avaliacao
        '''
        pass

    def excluir(self, id):
        '''
        Recebe o id de um filme e exclui o filme correspondente
        do banco de dados
        '''
        self.id = id
        resultado = session.query(Filme).get(id)
        if resultado is not None:
            print(f'ID: {resultado.id}\nTítulo: {resultado.titulo}\nEste filme está sendo excluído...')
        resultado = session.query(Filme).get(id)
        if resultado is not None:
            print('-' * 60)
            session.delete(resultado)
            session.commit()
            print('Filme excluído com sucesso')

    def buscar_todos(self):
        '''
        Realiza busca no banco de dados e retorna uma
        lista de objetos Filme com todos os registros,
        ordenados de forma crescente pelo titulo.
        '''
        lista = []
        resultado = session.query(Filme).order_by(Filme.titulo).all()
        for r in resultado:
            lista.append(r)
        return lista

    def buscar_por_id(self, id):
        '''
        Realiza busca no banco de dados e retorna um
        objeto Filme de acordo com o seu id
        '''
        self.id = id
        r = session.query(Filme).get(id)
        print('-' * 60)
        if r is not None:
            print(f'ID: {r.id} \nTítulo: {r.titulo} \nAno: {r.ano} \nGenero: {r.genero}')
        else:
            print('Não existe filme com este ID')

    def buscar_por_ano(self, ano):
        '''
        Realiza busca no banco de dados e retorna uma
        lista de objetos Filme de um ano específico,
        ordenado pelo ID de forma crescente
        '''
        lista = []
        self.ano = ano
        resultado = session.query(Filme).filter(Filme.ano == ano).order_by(Filme.id)
        for r in resultado:
            lista.append(r)
        return lista

    def buscar_por_genero(self, genero):
        '''
        Realiza busca no banco de dados e retorna uma
        lista de objetos Filme de um gênero específico,
        ordenados pelo titulo de forma crescente
        '''
        lista = []
        self.genero = genero
        resultado = session.query(Filme).filter(Filme.genero.like('%' + genero + '%')).order_by(Filme.titulo)
        for r in resultado:
            lista.append(r)
        return lista

    def buscar_por_elenco(self, ator):
        '''
        Realiza busca no banco de dados e retorna uma
        lista de objetos Filme que tenha um determinado ator/atriz como parte
        do elenco, ordenados pelo ano de lançamento em ordem crescente
        '''
        lista = []
        self.ator = ator
        resultado = session.query(Filme).filter(Filme.elenco.like('%' + ator + '%')).order_by(Filme.ano)
        for r in resultado:
            lista.append(r)
        return lista

    def buscar_melhores_do_ano(self, ano):
        '''
        Realiza busca no banco de dados e retorna uma lista de
        objetos Filme de um ano específico, com avaliação
        maior ou igual a 90
        Deve retornar ordenado pela avaliação de forma decrescente.
        DICA - utilize a função:
            .order_by(desc(Filme.avaliacao))
        '''
        lista = []
        self.ano = ano
        resultado = session.query(Filme).filter(Filme.ano == int(ano)).order_by(desc(Filme.avaliacao))
        for r in resultado:
            if r.avaliacao >= 90:
                lista.append(r)
        return lista

    def exportar_filmes(self, nome_arquivo):
        '''
        Exporta os dados contidos na tabela de filmes para um arquivo de texto
        O arquivo deve conter uma listagem dos filmes, ordenados pelos titulos
        dos filmes, contendo os dados de cada filme em uma linha, no formato:
        titulo;ano;genero;duracao;país;diretor;elenco;avaliacao;votos
        '''
        self.nome_arquivo = nome_arquivo
        arquivo = open(nome_arquivo, 'w', encoding='UTF-8')
        resultado = session.query(Filme).order_by(Filme.titulo).all()

        for r in resultado:
            arquivo.write(r.titulo + ';' + str(r.ano) + ';' + r.genero + ';' + str(r.duracao) + ';' + r.pais + ';' + r.diretor + ';' + r.elenco + ';' + str(r.avaliacao) + ';' + str(r.votos) + '\n')
        print('-'*60)
        print(f'Arquivo exportado com sucesso com o nome de {nome_arquivo}')
        print('-'*60)
        arquivo.close()
        connection.close()

    def importar_filmes(self, nome_arquivo):
        '''
        Recebe como parâmetro o nome de um arquivo de texto e importa os
        dados contidos no arquivo para o banco de dados.
        Considere que o arquivo contém uma listagem de filmes no formato:
        titulo;ano;genero;duracao;país;diretor;elenco;avaliacao;votos
        '''
        self.nome_arquivo = nome_arquivo
        arquivo = open(nome_arquivo, 'r', encoding='UTF-8')
        lista_filmes = []

        for linha in arquivo:
            lista = linha.split(';')
            film = Filme(lista[0], int(lista[1]), lista[2], int(lista[3]), lista[4], lista[5], lista[6], float(lista[7]), int(lista[8]))
            lista_filmes.append(film)

        session.add_all(lista_filmes)
        session.commit()


# EXEMPLO DE PROGRAMA PRINCIPAL
banco = BancoDeDados()
banco.criar_tabela()
banco.importar_filmes('movies.txt')

# Incluindo um filme com ano de 2019 e avaliação acima de 90
ReiLeao = Filme('O Rei leão', 2019, 'Animação, Aventura', 120, 'Brasil', 'Jon Fraveau', 'Ícaro Silva, Glauco Marques, Ivan Parente', 99, 599)
banco.incluir(ReiLeao)

# Incluindo uma lista de filmes com avaliação acima de 90
Vingadores = Filme('Vingadores: Ultimato', 2019, 'Ação, Fantasia, Aventura', 180, 'EUA', 'Joe Russo, Anthony Russo', 'Robert Downey Jr., Chris Evans, Mark Ruffalo', 100, 2578)
Eternos = Filme('Os Eternos', 2021, 'Ficção científica, Fantasia, Ação', 150, 'EUA', 'Chloé Zhao', 'Angelina Jolie, Richard Madden, Salma Hayek', 95, 678)
Mortal = Filme('Mortal Kombat', 2021, 'Animação, Aventura', 110, 'EUA', 'Simon McQuoid', 'Lewis Tan, Jessica McNamee, Josh Lawson', 92, 544)
lista_filmes = [Vingadores, Eternos, Mortal]
banco.incluir_lista(lista_filmes)
print('Estes são os filmes incluídos:')
for f in lista_filmes:
    print(f'\nID: {f.id} \nTítulo: {f.titulo} \nAno: {f.ano} \nGenero: {f.genero}')

# Busca todos os filmes
lista = banco.buscar_todos()
print('-'*60)
for f in lista:  # exibe lista de filmes
    print(f.id, f.titulo, f.ano, f.genero, f.duracao, f.pais, f.diretor, f.elenco, f.avaliacao, f.votos, '\n')

lista = banco.buscar_por_ano(2019)
print('-'*60)
for f in lista:         # exibe lista de filmes
    print(f.id, f.titulo, f.ano, f.genero, f.duracao, f.pais, f.diretor, f.elenco, f.avaliacao, f.votos)

# Busca por genero
lista = banco.buscar_por_genero('Romance')
print('-'*60)
for f in lista:         # exibe lista de filmes
    print(f.id, f.titulo, f.ano, f.genero)

# Busca por ator
lista = banco.buscar_por_elenco('Will')
print('-'*60)
for f in lista:         # exibe lista de filmes
    print(f.id, f.titulo, f.ano, f.genero, f.duracao, f.pais, f.diretor, f.elenco, f.avaliacao, f.votos)

# Busca melhores do ano
lista = banco.buscar_melhores_do_ano('2019')
print('-'*60)
for f in lista:         # exibe lista de filmes
    print(f.id, f.titulo, f.ano, f.genero, f.duracao, f.pais, f.diretor, f.elenco, f.avaliacao, f.votos)

# Buscar por id
f = banco.buscar_por_id(1002)
print('-' * 60)

# Excluir por id
f = banco.excluir(1002)
print('-' * 60)

# Exportar para um arquivo todos os filmes do banco
banco.exportar_filmes('saida.txt')
