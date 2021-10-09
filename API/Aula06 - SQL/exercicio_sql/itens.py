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
