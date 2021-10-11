from sqlalchemy import create_engine
from sqlalchemy import text

engine = create_engine('sqlite:///rpg.db')


class ItemNaoExisteException(Exception):
    pass


def consultar_item(id_item):
    with engine.connect() as conexao:
        consulta_db = text("SELECT * FROM Item WHERE id = :item")
        retorno_consulta = conexao.execute(consulta_db, item=id_item)
        items = retorno_consulta.fetchall()
        if items == []:
            raise ItemNaoExisteException
        else:
            items = items[0]
            return dict(items)


def nome_para_id_item(nome_item):
    with engine.connect() as conexao:
        consulta_db = text("SELECT * FROM Item WHERE nome = :nome")
        executa_consulta = conexao.execute(consulta_db, nome=nome_item)
        item = executa_consulta.fetchone()
        return int(item['id'])


def criar_item(tipo, nome, fisico, magia, agilidade):
    with engine.connect() as conexao:
        insert_db = text("INSERT INTO Item (tipo, nome, fisico, magia, agilidade, emUso) VALUES (:a, :b, :c, :d, :e, 0)")
        conexao.execute(insert_db, a=tipo, b=nome, c=fisico, d=magia, e=agilidade)
        pass


if __name__ == '__main__':
    print(nome_para_id_item('confortavel'))
