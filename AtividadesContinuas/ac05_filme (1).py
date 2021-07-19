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
        session.add(filme)
        session.commit()
        print('Filme incluído com sucesso')
        print('-' * 60)

    def incluir_lista(self, filmes):
        '''
        Recebe uma lista de objetos Filme e armazena esses
        objetos no banco de dados
        '''
        session.add_all(filmes)
        session.commit()
        print('Lista de filmes incluída com sucesso')
        print('-' * 60)

    def alterar_avaliacao(self, filme, avaliacao):
        '''
        Recebe um objeto filme e altera sua avaliação de
        acordo com o valor do parametro avaliacao
        '''
        resultado = session.query(Filme).get(filme.id)
        resultado.avaliacao = avaliacao
        session.commit()

    def excluir(self, id):
        '''
        Recebe o id de um filme e exclui o filme correspondente
        do banco de dados
        '''
        resultado = session.query(Filme).get(id)
        if resultado is not None:
            print(
                f'ID: {resultado.id}\nTítulo: {resultado.titulo}\nEste filme está sendo excluído...')
        resultado = session.query(Filme).get(id)
        if resultado is not None:
            session.delete(resultado)
            session.commit()

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
        r = session.query(Filme).get(id)
        print('-' * 60)
        if r is not None:
            print(
                f'ID: {r.id} \nTítulo: {r.titulo} \nAno: {r.ano} \nGenero: {r.genero} \nAvaliacao:{r.avaliacao}')
        else:
            print('Não existe filme com este ID')
        return r

    def buscar_por_ano(self, ano):
        '''
        Realiza busca no banco de dados e retorna uma
        lista de objetos Filme de um ano específico,
        ordenado pelo ID de forma crescente
        '''
        lista = []
        resultado = session.query(Filme).filter(
            Filme.ano == ano).order_by(Filme.id)
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
        resultado = session.query(Filme).filter(
            Filme.genero.like('%' + genero + '%')).order_by(Filme.titulo)
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
        resultado = session.query(Filme).filter(
            Filme.elenco.like('%' + ator + '%')).order_by(Filme.ano)
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
        resultado = session.query(Filme).filter(
            Filme.ano == int(ano)).order_by(desc(Filme.avaliacao))
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
        arquivo = open(nome_arquivo, 'w', encoding='UTF-8')
        resultado = session.query(Filme).order_by(Filme.titulo).all()

        for r in resultado:
            arquivo.write(r.titulo + ';' + str(r.ano) + ';' + r.genero + ';' + str(r.duracao) + ';' +
                          r.pais + ';' + r.diretor + ';' + r.elenco + ';' + str(r.avaliacao) + ';' + str(r.votos) + '\n')
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
            film = Filme(lista[0], int(lista[1]), lista[2], int(
                lista[3]), lista[4], lista[5], lista[6], float(lista[7]), int(lista[8]))
            lista_filmes.append(film)

        session.add_all(lista_filmes)
        session.commit()


# EXEMPLO DE PROGRAMA PRINCIPAL
banco = BancoDeDados()
banco.criar_tabela()
banco.importar_filmes('movies.txt')

# Cria um novo Filme e insere no banco de dados
filme1 = Filme("Parasite", 2019, "Comedy, Drama, Thriller", 132, "Korea",
               "Bong Joon Ho", "Song Kang-ho, Jang Hye-jin, Choi Woo-shik", 92, 40273)
banco.incluir(filme1)

filme2 = Filme("Joker", 2019, 'Crime, Drama, Thriller', 122, "USA",
               "Todd Phillips", "Joaquin Phoenix, Robert De Niro, Zazie Beetz", 91, 78481)
filme3 = Filme("Avengers: Endgame", 2019, 'Drama, Thriller', 181, "USA",
               "Anthony Russo, Joe Russo", "Robert Downey Jr., Chris Evans, Mark Ruffalo", 93, 715250)
lista_filmes = [filme2, filme3]
banco.incluir_lista(lista_filmes)

# Incluindo um filme com ano de 2019 e avaliação acima de 90
ReiLeao = Filme('O Rei leão', 2019, 'Animação, Aventura', 120, 'Brasil',
                'Jon Fraveau', 'Ícaro Silva, Glauco Marques, Ivan Parente', 99, 599)
banco.incluir(ReiLeao)

# Incluindo uma lista de filmes com avaliação acima de 90
Vingadores = Filme('Vingadores: Ultimato', 2019, 'Ação, Fantasia, Aventura', 180, 'EUA',
                   'Joe Russo, Anthony Russo', 'Robert Downey Jr., Chris Evans, Mark Ruffalo', 91, 2578)
Eternos = Filme('Os Eternos', 2021, 'Ficção científica, Fantasia, Ação', 150,
                'EUA', 'Chloé Zhao', 'Angelina Jolie, Richard Madden, Salma Hayek', 95, 678)
Mortal = Filme('Mortal Kombat', 2021, 'Animação, Aventura', 110, 'EUA',
               'Simon McQuoid', 'Lewis Tan, Jessica McNamee, Josh Lawson', 92, 544)
lista_filmes = [Vingadores, Eternos, Mortal]
banco.incluir_lista(lista_filmes)

# Altera a avalação do filme de id 7 para 98
filme = banco.buscar_por_id(7)
if filme is not None:
    banco.alterar_avaliacao(filme, 98)
filme = banco.buscar_por_id(7)

# Exclui o filme de id 6
banco.excluir(6)

# Busca todos os filmes
lista = banco.buscar_todos()
print('-'*60)
for f in lista:  # exibe lista de filmes
    print(f.id, f.titulo, f.ano, f.genero, f.duracao,
          f.pais, f.diretor, f.elenco, f.avaliacao, f.votos)

# Busca todos os filmes do ano de 2019
lista = banco.buscar_por_ano(2019)
print('-'*60)
for f in lista:         # exibe lista de filmes
    print(f.id, f.titulo, f.ano)

# Busca por genero
lista = banco.buscar_por_genero('Crime')
print('-'*60)
for f in lista:         # exibe lista de filmes
    print(f.id, f.titulo, f.ano, f.genero)

# Busca todos os filmes com participação da atriz de nome 'Nicole Balsam'
lista = banco.buscar_por_elenco('Nicole Balsam')
print('-'*60)
for f in lista:         # exibe lista de filmes
    print(f.id, f.titulo, f.ano, f.elenco)

# Busca melhores do ano
lista = banco.buscar_melhores_do_ano('2019')
print('-'*60)
for f in lista:         # exibe lista de filmes
    print(f.id, f.titulo, f.ano, f.avaliacao)

# Buscar por id
f = banco.buscar_por_id(50)
print('-' * 60)

# Excluir por id
f = banco.excluir(37)
print('-' * 60)

# Alterando avaliacao de um filme
print('-' * 60)
print(f'Título: {Vingadores.titulo} e avaliação: {Vingadores.avaliacao}')
print('-' * 60)
f = banco.alterar_avaliacao(Vingadores, 100)

# mostrando os filmes adicionados
f = banco.buscar_por_id(1001)
print('-' * 60)
f = banco.buscar_por_id(1002)
print('-' * 60)
f = banco.buscar_por_id(1003)
print('-' * 60)
f = banco.buscar_por_id(1004)
print('-' * 60)

# Exportar para um arquivo todos os filmes do banco
banco.exportar_filmes('saida.txt')

# Altera a avalação do filme de id 7 para 98
filme = banco.buscar_por_id(7)
if filme is not None:
    banco.alterar_avaliacao(filme, 98)
