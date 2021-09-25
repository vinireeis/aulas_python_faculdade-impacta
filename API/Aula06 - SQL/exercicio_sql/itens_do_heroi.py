from sqlalchemy import text
from sqlalchemy import create_engine

engine = create_engine('sqlite:///rpg.db')

class ItemNaoExisteException(Exception):
    pass

def heroi_tem_item(heroi_id):
    with engine.connect() as conexao:
        query = text("SELECT * FROM ItemDoHeroi WHERE idHeroi = :idHeroi")
        tapa_buraco = conexao.execute(query, idHeroi = heroi_id)
        herois = tapa_buraco.fetchall()
        if herois == []:
            return False
        else:
            return True

def heroi_quantos_itens(id_heroi):
    with engine.connect()  as conexao:
        query = text("SELECT * FROM ItemDoHeroi WHERE IdHeroi = :idHeroi")
        tapa_buraco = conexao.execute(query, idHeroi = id_heroi)
        herois = tapa_buraco.fetchone()
        cont = 0
        while herois != None:
            if dict(herois)['idHeroi'] == id_heroi:
                cont += 1
                herois = tapa_buraco.fetchone()
            else:
                break
        return cont
